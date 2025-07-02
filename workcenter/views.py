from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod
from .forms import WorkCenterForm, ClassroomForm, SchoolCycleForm, SchoolPeriodForm

# Vistas principales del módulo de centro de trabajo

@login_required
def dashboard(request):
    """
    Muestra el dashboard principal del módulo de centro de trabajo.
    Lista todos los centros de trabajo, aulas, ciclos y periodos escolares.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template dashboard.html
    """
    work_centers = WorkCenter.objects.all()
    return render(request, 'workcenter/dashboard.html', {
        'work_centers': work_centers
    })

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
            messages.success(request, 'Centro de trabajo actualizado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = WorkCenterForm(instance=workcenter)
    return render(request, 'workcenter/workcenter_form.html', {
        'form': form,
        'title': 'Actualizar Centro de Trabajo'
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

# Funciones de gestión de ciclos escolares

@login_required
def schoolcycle_create(request):
    """
    Crea un nuevo ciclo escolar en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = SchoolCycleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ciclo escolar creado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = SchoolCycleForm()
    return render(request, 'workcenter/schoolcycle_form.html', {
        'form': form,
        'title': 'Crear Ciclo Escolar'
    })

@login_required
def schoolcycle_update(request, pk):
    """
    Actualiza un ciclo escolar existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del ciclo escolar a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    schoolcycle = get_object_or_404(SchoolCycle, pk=pk)
    if request.method == 'POST':
        form = SchoolCycleForm(request.POST, instance=schoolcycle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ciclo escolar actualizado exitosamente')
            return redirect('workcenter:dashboard')
    else:
        form = SchoolCycleForm(instance=schoolcycle)
    return render(request, 'workcenter/schoolcycle_form.html', {
        'form': form,
        'title': 'Actualizar Ciclo Escolar'
    })

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
