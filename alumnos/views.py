from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from .models import Alumno
from .forms import AlumnoRegistrationForm, AlumnoUpdateForm
from datetime import datetime


@login_required
def alumno_list(request):
    """Vista para listar todos los alumnos."""
    alumnos = Alumno.objects.select_related('user', 'programa_academico').all()
    
    # Estadísticas
    total_alumnos = alumnos.count()
    alumnos_por_programa = alumnos.values('programa_academico__nombre').annotate(
        count=Count('id')
    ).order_by('-count')
    
    context = {
        'alumnos': alumnos,
        'total_alumnos': total_alumnos,
        'alumnos_por_programa': alumnos_por_programa,
    }
    return render(request, 'alumnos/alumno_list.html', context)


@login_required
def alumno_detail(request, pk):
    """Vista para mostrar detalles de un alumno."""
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumnos/alumno_detail.html', {'alumno': alumno})


@login_required
def alumno_create(request):
    """Vista para crear un nuevo alumno."""
    if request.method == 'POST':
        form = AlumnoRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear el usuario con username temporal
            user = form.save(commit=False)
            user.username = f"temp_{datetime.now().strftime('%Y%m%d%H%M%S')}"  # Username temporal
            user.save()
            
            # Crear el alumno (el número de cuenta se genera automáticamente)
            alumno = Alumno.objects.create(
                user=user,
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                work_center=form.cleaned_data['work_center'],
                programa_academico=form.cleaned_data['programa_academico'],
                curp=form.cleaned_data['curp'],
                telefono_contacto=form.cleaned_data.get('telefono_contacto', ''),
                nombre_contacto_emergencia=form.cleaned_data.get('nombre_contacto_emergencia', ''),
                telefono_contacto_emergencia=form.cleaned_data.get('telefono_contacto_emergencia', ''),
                foto=form.cleaned_data.get('foto')
            )
            
            # Actualizar el username del usuario con el número de cuenta
            user.username = alumno.numero_cuenta
            user.save()
            
            messages.success(request, _('Alumno registrado exitosamente.'))
            return redirect('alumnos:alumno_list')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = AlumnoRegistrationForm()
    
    return render(request, 'alumnos/alumno_form.html', {
        'form': form,
        'title': _('Registrar Nuevo Alumno'),
        'submit_text': _('Registrar Alumno')
    })


@login_required
def alumno_update(request, pk):
    """Vista para actualizar un alumno existente."""
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == 'POST':
        form = AlumnoUpdateForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            # Actualizar datos del usuario
            alumno.user.first_name = form.cleaned_data['first_name']
            alumno.user.last_name = form.cleaned_data['last_name']
            alumno.user.email = form.cleaned_data['email']
            alumno.user.save()
            
            # Actualizar datos del alumno
            form.save()
            
            messages.success(request, _('Alumno actualizado exitosamente.'))
            return redirect('alumnos:alumno_list')
        else:
            messages.error(request, _('Por favor corrige los errores en el formulario.'))
    else:
        form = AlumnoUpdateForm(instance=alumno)
    
    return render(request, 'alumnos/alumno_form.html', {
        'form': form,
        'alumno': alumno,
        'title': _('Editar Alumno'),
        'submit_text': _('Actualizar Alumno')
    })


@login_required
def alumno_delete(request, pk):
    """Vista para eliminar un alumno."""
    alumno = get_object_or_404(Alumno, pk=pk)
    
    if request.method == 'POST':
        # Eliminar el usuario asociado
        user = alumno.user
        alumno.delete()
        user.delete()
        
        messages.success(request, _('Alumno eliminado exitosamente.'))
        return redirect('alumnos:alumno_list')
    
    return render(request, 'alumnos/alumno_confirm_delete.html', {
        'alumno': alumno
    })


@login_required
def alumno_dashboard(request):
    """Dashboard para gestión de alumnos."""
    # Estadísticas
    total_alumnos = Alumno.objects.count()
    alumnos_por_programa = Alumno.objects.values('programa_academico__nombre').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    # Últimos alumnos registrados
    ultimos_alumnos = Alumno.objects.select_related('user', 'programa_academico').order_by('-user__date_joined')[:5]
    
    context = {
        'total_alumnos': total_alumnos,
        'alumnos_por_programa': alumnos_por_programa,
        'ultimos_alumnos': ultimos_alumnos,
    }
    return render(request, 'alumnos/alumno_dashboard.html', context) 