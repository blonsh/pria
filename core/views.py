from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from core.decorators import role_required
from core.utils import UserRoles
from core.forms import UserRegistrationForm, AlumnoRegistrationForm, DocenteRegistrationForm, MatriculaForm, BuscarMatriculaForm
from django.contrib.auth.models import Group, User
from django.db.models import Count, Q
from django.core.paginator import Paginator
from .models import UserProfile, Carrera, Materia, Docente, Alumno, Curso, Matricula, ActivityLog
from django.utils import timezone
from datetime import timedelta

def login_view(request):
    """Vista para iniciar sesión."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, _('Credenciales inválidas'))
            
    return render(request, 'core/login.html')

@login_required
def logout_view(request):
    """Vista para cerrar sesión."""
    logout(request)
    return redirect('core:login')

def home(request):
    """Vista principal del sistema."""
    context = {
        'total_usuarios': User.objects.count(),
        'total_alumnos': Alumno.objects.count(),
        'total_docentes': Docente.objects.count(),
        'total_carreras': 0   # TODO: Implementar cuando los modelos estén disponibles
    }
    return render(request, 'core/home.html', context)

@login_required
@role_required(UserRoles.ADMIN)
def register_user(request):
    """Vista para el registro de usuarios."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Usuario registrado exitosamente.'))
            return redirect('login')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = UserRegistrationForm()
    
    return render(request, 'core/register_user.html', {'form': form})

@login_required
@role_required(UserRoles.ADMIN)
def register_alumno(request):
    """Vista para el registro de alumnos."""
    if request.method == 'POST':
        form = AlumnoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Alumno registrado exitosamente.'))
            return redirect('login')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = AlumnoRegistrationForm()
    
    return render(request, 'core/register_alumno.html', {'form': form})

@login_required
@role_required(UserRoles.ADMIN)
def register_docente(request):
    """Vista para el registro de docentes."""
    if request.method == 'POST':
        form = DocenteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Docente registrado exitosamente.'))
            return redirect('login')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = DocenteRegistrationForm()
    
    return render(request, 'core/register_docente.html', {'form': form})

@login_required
def matricula_list(request):
    """Vista para listar todas las matrículas."""
    # Obtener parámetros de búsqueda
    form = BuscarMatriculaForm(request.GET)
    matriculas = Matricula.objects.select_related('alumno__user', 'curso__materia', 'curso__docente__user').all()
    
    # Aplicar filtros si se proporcionan
    if form.is_valid():
        if form.cleaned_data.get('alumno'):
            matriculas = matriculas.filter(alumno=form.cleaned_data['alumno'])
        if form.cleaned_data.get('curso'):
            matriculas = matriculas.filter(curso=form.cleaned_data['curso'])
        if form.cleaned_data.get('fecha_inicio'):
            matriculas = matriculas.filter(fecha_matricula__gte=form.cleaned_data['fecha_inicio'])
        if form.cleaned_data.get('fecha_fin'):
            matriculas = matriculas.filter(fecha_matricula__lte=form.cleaned_data['fecha_fin'])
    
    # Estadísticas
    total_matriculas = matriculas.count()
    matriculas_por_curso = matriculas.values('curso__materia__nombre').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Paginación
    paginator = Paginator(matriculas, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'matriculas': page_obj,
        'total_matriculas': total_matriculas,
        'matriculas_por_curso': matriculas_por_curso,
        'form': form,
    }
    return render(request, 'core/matricula_list.html', context)

@login_required
def matricula_create(request):
    """Vista para crear una nueva matrícula."""
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            matricula = form.save()
            messages.success(request, _('Alumno matriculado exitosamente en el curso.'))
            return redirect('core:matricula_list')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = MatriculaForm()
    
    return render(request, 'core/matricula_form.html', {
        'form': form,
        'title': _('Matricular Alumno'),
        'submit_text': _('Matricular')
    })

@login_required
def matricula_detail(request, pk):
    """Vista para mostrar detalles de una matrícula."""
    matricula = get_object_or_404(Matricula, pk=pk)
    return render(request, 'core/matricula_detail.html', {'matricula': matricula})

@login_required
def matricula_delete(request, pk):
    """Vista para eliminar una matrícula."""
    matricula = get_object_or_404(Matricula, pk=pk)
    
    if request.method == 'POST':
        alumno_nombre = f"{matricula.alumno.user.first_name} {matricula.alumno.user.last_name}"
        curso_nombre = str(matricula.curso)
        matricula.delete()
        
        messages.success(request, _('Matrícula eliminada exitosamente.'))
        return redirect('core:matricula_list')
    
    return render(request, 'core/matricula_confirm_delete.html', {
        'matricula': matricula
    })

@login_required
def matricula_dashboard(request):
    """Dashboard para gestión de matrículas."""
    # Estadísticas generales
    total_matriculas = Matricula.objects.count()
    total_alumnos = Alumno.objects.count()
    total_cursos = Curso.objects.count()
    
    # Matrículas por curso
    matriculas_por_curso = Matricula.objects.values('curso__materia__nombre').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Últimas matrículas
    ultimas_matriculas = Matricula.objects.select_related(
        'alumno__user', 'curso__materia'
    ).order_by('-fecha_matricula')[:5]
    
    # Cursos con más demanda
    cursos_demanda = Curso.objects.annotate(
        matriculados=Count('matricula')
    ).filter(matriculados__gt=0).order_by('-matriculados')[:5]
    
    context = {
        'total_matriculas': total_matriculas,
        'total_alumnos': total_alumnos,
        'total_cursos': total_cursos,
        'matriculas_por_curso': matriculas_por_curso,
        'ultimas_matriculas': ultimas_matriculas,
        'cursos_demanda': cursos_demanda,
    }
    return render(request, 'core/matricula_dashboard.html', context)

@login_required
def reportes_dashboard(request):
    """
    Dashboard principal de reportes del sistema.
    Proporciona acceso a todos los reportes disponibles.
    """
    # Estadísticas generales para el dashboard
    total_usuarios = User.objects.count()
    total_alumnos = Alumno.objects.count()
    total_docentes = Docente.objects.count()
    total_matriculas = Matricula.objects.count()
    
    # Estadísticas de asistencia (si el modelo existe)
    try:
        from asistencia.models import Asistencia
        total_asistencias = Asistencia.objects.count()
    except ImportError:
        total_asistencias = 0
    
    # Estadísticas de planes de estudio (si el modelo existe)
    try:
        from planes_estudio.models import PlanEstudio
        total_planes = PlanEstudio.objects.count()
        planes_activos = PlanEstudio.objects.filter(estado='ACTIVO').count()
    except ImportError:
        total_planes = 0
        planes_activos = 0
    
    # Estadísticas de centros de trabajo (si el modelo existe)
    try:
        from workcenter.models import WorkCenter
        total_workcenters = WorkCenter.objects.count()
    except ImportError:
        total_workcenters = 0
    
    context = {
        'total_usuarios': total_usuarios,
        'total_alumnos': total_alumnos,
        'total_docentes': total_docentes,
        'total_matriculas': total_matriculas,
        'total_asistencias': total_asistencias,
        'total_planes': total_planes,
        'planes_activos': planes_activos,
        'total_workcenters': total_workcenters,
    }
    
    return render(request, 'core/reportes_dashboard.html', context)

@login_required
def logs_dashboard(request):
    """
    Dashboard para consultar logs de actividades de los usuarios.
    Permite filtrar por fecha, usuario, acción y módulo.
    """
    # Obtener parámetros de filtro
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    usuario = request.GET.get('usuario')
    accion = request.GET.get('accion')
    modulo = request.GET.get('modulo')
    search = request.GET.get('search')
    
    # Query base
    logs = ActivityLog.objects.select_related('user').all()
    
    # Aplicar filtros
    if fecha_inicio:
        logs = logs.filter(timestamp__date__gte=fecha_inicio)
    if fecha_fin:
        logs = logs.filter(timestamp__date__lte=fecha_fin)
    if usuario:
        logs = logs.filter(user__username__icontains=usuario)
    if accion:
        logs = logs.filter(action=accion)
    if modulo:
        logs = logs.filter(module=modulo)
    if search:
        logs = logs.filter(
            Q(description__icontains=search) |
            Q(object_name__icontains=search) |
            Q(object_type__icontains=search)
        )
    
    # Estadísticas
    total_logs = logs.count()
    logs_hoy = ActivityLog.objects.filter(timestamp__date=timezone.now().date()).count()
    logs_semana = ActivityLog.objects.filter(
        timestamp__date__gte=timezone.now().date() - timedelta(days=7)
    ).count()
    
    # Logs por acción
    logs_por_accion = logs.values('action').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Logs por módulo
    logs_por_modulo = logs.values('module').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Usuarios más activos
    usuarios_activos = logs.values('user__username').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Paginación
    paginator = Paginator(logs, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'logs': page_obj,
        'total_logs': total_logs,
        'logs_hoy': logs_hoy,
        'logs_semana': logs_semana,
        'logs_por_accion': logs_por_accion,
        'logs_por_modulo': logs_por_modulo,
        'usuarios_activos': usuarios_activos,
        'filtros': {
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'usuario': usuario,
            'accion': accion,
            'modulo': modulo,
            'search': search,
        },
        'acciones': ActivityLog.ACTION_CHOICES,
        'modulos': ActivityLog.MODULE_CHOICES,
    }
    
    return render(request, 'core/logs_dashboard.html', context)
