from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Role, User
from .forms import RoleForm, UserForm

# Vistas principales del módulo de usuarios

@login_required
def dashboard(request):
    """
    Muestra el dashboard principal del módulo de usuarios.
    Lista todos los roles y usuarios existentes en el sistema.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el template dashboard.html
    """
    roles = Role.objects.all()
    users = User.objects.all()
    return render(request, 'users/dashboard.html', {
        'roles': roles,
        'users': users
    })

# Funciones de gestión de roles

@login_required
def role_create(request):
    """
    Crea un nuevo rol en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado exitosamente')
            return redirect('users:dashboard')
    else:
        form = RoleForm()
    return render(request, 'users/role_form.html', {
        'form': form,
        'title': 'Crear Rol'
    })

@login_required
def role_update(request, pk):
    """
    Actualiza un rol existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del rol a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente')
            return redirect('users:dashboard')
    else:
        form = RoleForm(instance=role)
    return render(request, 'users/role_form.html', {
        'form': form,
        'title': 'Actualizar Rol'
    })

# Funciones de gestión de usuarios

@login_required
def user_create(request):
    """
    Crea un nuevo usuario en el sistema.
    Maneja tanto el GET como el POST para mostrar el formulario y procesar el envío.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('users:dashboard')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Crear Usuario'
    })

@login_required
def user_update(request, pk):
    """
    Actualiza un usuario existente en el sistema.
    
    Args:
        request: Objeto HttpRequest
        pk: ID del usuario a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirige al dashboard
    """
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente')
            return redirect('users:dashboard')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Actualizar Usuario'
    })
