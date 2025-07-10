from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod, SchoolCycleConfig
from .forms import WorkCenterForm, ClassroomForm, SchoolCycleForm, SchoolPeriodForm, SchoolCycleConfigForm
from datetime import date

# Vistas principales del módulo de centro de trabajo

@login_required
def dashboard(request):
    """
    Dashboard principal del módulo de centros de trabajo.
    Muestra estadísticas y enlaces rápidos a las funcionalidades principales.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template dashboard.html
    """
    # Obtener estadísticas
    total_workcenters = WorkCenter.objects.count()
    total_classrooms = Classroom.objects.count()
    total_school_cycles = SchoolCycle.objects.count()
    total_school_periods = SchoolPeriod.objects.count()
    
    # Obtener datos recientes
    recent_workcenters = WorkCenter.objects.all().order_by('-id')[:5]
    recent_classrooms = Classroom.objects.all().order_by('-id')[:5]
    recent_school_cycles = SchoolCycle.objects.all().order_by('-start_date')[:5]
    
    context = {
        'total_workcenters': total_workcenters,
        'total_classrooms': total_classrooms,
        'total_school_cycles': total_school_cycles,
        'total_school_periods': total_school_periods,
        'recent_workcenters': recent_workcenters,
        'recent_classrooms': recent_classrooms,
        'recent_school_cycles': recent_school_cycles,
    }
    
    return render(request, 'workcenter/dashboard.html', context)

@login_required
def workcenter_list(request):
    """
    Lista todos los centros de trabajo en el sistema.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template workcenter_list.html
    """
    work_centers = WorkCenter.objects.all().order_by('name')
    return render(request, 'workcenter/workcenter_list.html', {
        'work_centers': work_centers
    })

@login_required
def workcenter_detail(request, pk):
    """
    Muestra los detalles de un centro de trabajo específico.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del centro de trabajo a mostrar
        
    Returns:
        HttpResponse: Renderiza el template workcenter_detail.html
    """
    workcenter = get_object_or_404(WorkCenter, pk=pk)
    
    # Obtener aulas y ciclos escolares relacionados
    classrooms = workcenter.classroom_set.all().order_by('name')
    school_cycles = workcenter.schoolcycle_set.all().order_by('-start_date')
    
    context = {
        'workcenter': workcenter,
        'classrooms': classrooms,
        'school_cycles': school_cycles,
    }
    
    return render(request, 'workcenter/workcenter_detail.html', context)

# Funciones de gestión de centros de trabajo

@login_required
def workcenter_create(request):
    """
    Crea un nuevo centro de trabajo en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = WorkCenterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Centro de trabajo creado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = WorkCenterForm()
    return render(request, 'workcenter/workcenter_form.html', {
        'form': form,
        'title': 'Crear Centro de Trabajo'
    })

@login_required
def workcenter_update(request, pk):
    """
    Actualiza un centro de trabajo existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del centro de trabajo a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    workcenter = get_object_or_404(WorkCenter, pk=pk)
    
    if request.method == 'POST':
        form = WorkCenterForm(request.POST, instance=workcenter)
        if form.is_valid():
            form.save()
            messages.success(request, f'Centro de trabajo "{workcenter.name}" actualizado exitosamente')
            return redirect('workcenter:workcenter_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = WorkCenterForm(instance=workcenter)
    
    return render(request, 'workcenter/workcenter_form.html', {
        'form': form,
        'workcenter': workcenter,
        'title': 'Actualizar Centro de Trabajo',
        'is_update': True
    })

# Funciones de gestión de aulas

@login_required
def classroom_create(request):
    """
    Crea una nueva aula en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula creada exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = ClassroomForm()
    return render(request, 'workcenter/classroom_form.html', {
        'form': form,
        'title': 'Crear Aula'
    })

@login_required
def classroom_update(request, pk):
    """
    Actualiza una aula existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID de la aula a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula actualizada exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'workcenter/classroom_form.html', {
        'form': form,
        'title': 'Actualizar Aula'
    })

@login_required
def classroom_list(request):
    """
    Lista todas las aulas del sistema.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template classroom_list.html
    """
    classrooms = Classroom.objects.all().select_related('work_center').order_by('work_center__name', 'name')
    
    # Estadísticas
    total_classrooms = classrooms.count()
    total_capacity = sum(classroom.capacity for classroom in classrooms)
    avg_capacity = total_capacity / total_classrooms if total_classrooms > 0 else 0
    
    context = {
        'classrooms': classrooms,
        'total_classrooms': total_classrooms,
        'total_capacity': total_capacity,
        'avg_capacity': round(avg_capacity, 1),
    }
    
    return render(request, 'workcenter/classroom_list.html', context)

# Funciones de gestión de ciclos escolares

@login_required
def schoolcycle_create(request):
    """
    Crea un nuevo ciclo escolar en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige a la lista de ciclos
    """
    if request.method == 'POST':
        form = SchoolCycleForm(request.POST)
        if form.is_valid():
            cycle = form.save()
            messages.success(request, f'Ciclo escolar "{cycle.name}" creado exitosamente')
            return redirect('workcenter:schoolcycle_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = SchoolCycleForm()
    return render(request, 'workcenter/schoolcycle_form.html', {
        'form': form,
        'title': 'Crear Ciclo Escolar',
        'is_update': False,
        'today': date.today(),
    })

@login_required
def schoolcycle_update(request, pk):
    """
    Actualiza un ciclo escolar existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del ciclo escolar a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige a la lista de ciclos
    """
    schoolcycle = get_object_or_404(SchoolCycle, pk=pk)
    
    if request.method == 'POST':
        form = SchoolCycleForm(request.POST, instance=schoolcycle)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ciclo escolar "{schoolcycle.name}" actualizado exitosamente')
            return redirect('workcenter:schoolcycle_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = SchoolCycleForm(instance=schoolcycle)
    
    return render(request, 'workcenter/schoolcycle_form.html', {
        'form': form,
        'title': 'Actualizar Ciclo Escolar',
        'schoolcycle': schoolcycle,
        'is_update': True,
        'today': date.today(),
        'duration_days': (schoolcycle.end_date - schoolcycle.start_date).days,
    })

@login_required
def schoolcycle_list(request):
    """
    Lista todos los ciclos escolares del sistema.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template schoolcycle_list.html
    """
    school_cycles = SchoolCycle.objects.all().select_related('work_center').order_by('-start_date', 'work_center__name')
    
    # Estadísticas
    total_cycles = school_cycles.count()
    active_cycles = school_cycles.filter(
        start_date__lte=date.today(),
        end_date__gte=date.today()
    ).count()
    
    # Obtener ciclos activos por configuración
    active_cycles_by_config = []
    for work_center in WorkCenter.objects.all():
        config, created = SchoolCycleConfig.objects.get_or_create(work_center=work_center)
        active_cycles_for_center = config.get_active_cycles()
        if active_cycles_for_center.exists():
            active_cycles_by_config.extend(active_cycles_for_center)
    
    # Calcular duración promedio y agregar duración a cada ciclo
    total_duration = 0
    for cycle in school_cycles:
        duration = (cycle.end_date - cycle.start_date).days
        cycle.duration_days = duration
        total_duration += duration
    
    avg_duration = total_duration / total_cycles if total_cycles > 0 else 0
    
    context = {
        'school_cycles': school_cycles,
        'total_cycles': total_cycles,
        'active_cycles': active_cycles,
        'active_cycles_by_config': active_cycles_by_config,
        'avg_duration': round(avg_duration, 1),
        'today': date.today(),
    }
    
    return render(request, 'workcenter/schoolcycle_list.html', context)

@login_required
def cycle_config_list(request):
    """
    Lista todas las configuraciones de ciclos por centro de trabajo.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template cycle_config_list.html
    """
    work_centers = WorkCenter.objects.all().prefetch_related('cycle_config', 'schoolcycle_set')
    
    # Crear configuraciones para centros que no las tengan
    for work_center in work_centers:
        SchoolCycleConfig.objects.get_or_create(work_center=work_center)
    
    # Refrescar la consulta para incluir las configuraciones creadas
    work_centers = WorkCenter.objects.all().prefetch_related('cycle_config', 'schoolcycle_set')
    
    context = {
        'work_centers': work_centers,
        'today': date.today(),
    }
    
    return render(request, 'workcenter/cycle_config_list.html', context)

@login_required
def cycle_config_update(request, work_center_id):
    """
    Actualiza la configuración de ciclos para un centro de trabajo específico.
    
    Args:
        request: Objeto HttpRequest
        work_center_id: ID del centro de trabajo
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige a la lista
    """
    work_center = get_object_or_404(WorkCenter, pk=work_center_id)
    config, created = SchoolCycleConfig.objects.get_or_create(work_center=work_center)
    
    if request.method == 'POST':
        form = SchoolCycleConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, f'Configuración de ciclos para "{work_center.name}" actualizada exitosamente')
            return redirect('workcenter:cycle_config_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario')
    else:
        form = SchoolCycleConfigForm(instance=config)
    
    # Obtener ciclos activos para mostrar en el contexto
    active_cycles = config.get_active_cycles()
    
    context = {
        'form': form,
        'work_center': work_center,
        'config': config,
        'active_cycles': active_cycles,
        'title': f'Configurar Ciclos - {work_center.name}',
    }
    
    return render(request, 'workcenter/cycle_config_form.html', context)

@login_required
def cycle_activation_management(request, work_center_id):
    """
    Gestiona la activación manual de ciclos para un centro de trabajo.
    
    Args:
        request: Objeto HttpRequest
        work_center_id: ID del centro de trabajo
        
    Returns:
        HttpResponse: Renderiza el template de gestión de activación
    """
    work_center = get_object_or_404(WorkCenter, pk=work_center_id)
    config, created = SchoolCycleConfig.objects.get_or_create(work_center=work_center)
    
    if request.method == 'POST':
        # Procesar activación/desactivación de ciclos
        cycle_ids = request.POST.getlist('active_cycles')
        
        # Desactivar todos los ciclos del centro
        SchoolCycle.objects.filter(work_center=work_center).update(is_active=False)
        
        # Activar solo los seleccionados
        if cycle_ids:
            SchoolCycle.objects.filter(
                work_center=work_center,
                id__in=cycle_ids
            ).update(is_active=True)
        
        messages.success(request, f'Ciclos activos para "{work_center.name}" actualizados exitosamente')
        return redirect('workcenter:cycle_config_list')
    
    # Obtener todos los ciclos del centro
    cycles = SchoolCycle.objects.filter(work_center=work_center).order_by('-start_date')
    active_cycles = config.get_active_cycles()
    
    context = {
        'work_center': work_center,
        'config': config,
        'cycles': cycles,
        'active_cycles': active_cycles,
        'title': f'Gestionar Ciclos Activos - {work_center.name}',
    }
    
    return render(request, 'workcenter/cycle_activation_management.html', context)

# Funciones de gestión de periodos escolares

@login_required
def schoolperiod_create(request):
    """
    Crea un nuevo periodo escolar en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = SchoolPeriodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Periodo escolar creado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = SchoolPeriodForm()
    return render(request, 'workcenter/schoolperiod_form.html', {
        'form': form,
        'title': 'Crear Periodo Escolar'
    })

@login_required
def schoolperiod_update(request, pk):
    """
    Actualiza un periodo escolar existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del periodo escolar a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    schoolperiod = get_object_or_404(SchoolPeriod, pk=pk)
    if request.method == 'POST':
        form = SchoolPeriodForm(request.POST, instance=schoolperiod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Periodo escolar actualizado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = SchoolPeriodForm(instance=schoolperiod)
    return render(request, 'workcenter/schoolperiod_form.html', {
        'form': form,
        'title': 'Actualizar Periodo Escolar'
    })

# Funciones de Control Escolar

@login_required
def control_escolar_dashboard(request):
    """
    Dashboard principal del módulo de Control Escolar.
    Muestra estadísticas y enlaces rápidos a las funcionalidades de control escolar.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template control_escolar_dashboard.html
    """
    # Obtener estadísticas de control escolar
    total_workcenters = WorkCenter.objects.count()
    total_alumnos = 0  # Aquí podrías agregar la lógica para contar alumnos
    total_ciclos_activos = SchoolCycle.objects.filter(is_active=True).count()
    
    # Obtener centros de trabajo con información de control escolar
    work_centers = WorkCenter.objects.all().order_by('name')
    
    context = {
        'total_workcenters': total_workcenters,
        'total_alumnos': total_alumnos,
        'total_ciclos_activos': total_ciclos_activos,
        'work_centers': work_centers,
    }
    
    return render(request, 'workcenter/control_escolar_dashboard.html', context)

@login_required
def kardex_view(request):
    """
    Vista principal del Kardex.
    Permite consultar y gestionar el historial académico de los alumnos.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template kardex.html
    """
    # Obtener parámetros de búsqueda
    search_query = request.GET.get('search', '')
    work_center_id = request.GET.get('work_center', '')
    ciclo_id = request.GET.get('ciclo', '')
    
    # Obtener centros de trabajo y ciclos para los filtros
    work_centers = WorkCenter.objects.all().order_by('name')
    ciclos = SchoolCycle.objects.filter(is_active=True).order_by('-start_date')
    
    # Aquí implementarías la lógica para obtener datos del kardex
    # Por ahora, creamos datos de ejemplo
    kardex_data = []
    
    # Si hay búsqueda, simular resultados
    if search_query:
        # Aquí agregarías la lógica real de búsqueda en la base de datos
        kardex_data = [
            {
                'alumno': 'Juan Pérez',
                'numero_cuenta': '24-01-00001',
                'programa': 'Ingeniería en Sistemas',
                'ciclo': '2024-2025',
                'promedio': 8.5,
                'materias_aprobadas': 45,
                'materias_reprobadas': 2,
            },
            {
                'alumno': 'María García',
                'numero_cuenta': '24-01-00002',
                'programa': 'Administración',
                'ciclo': '2024-2025',
                'promedio': 9.2,
                'materias_aprobadas': 48,
                'materias_reprobadas': 0,
            }
        ]
    
    context = {
        'search_query': search_query,
        'work_centers': work_centers,
        'ciclos': ciclos,
        'selected_work_center': work_center_id,
        'selected_ciclo': ciclo_id,
        'kardex_data': kardex_data,
        'total_results': len(kardex_data),
    }
    
    return render(request, 'workcenter/kardex.html', context)
