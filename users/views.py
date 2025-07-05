from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
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

def get_permissions_by_module():
    """
    Agrupa los permisos por módulo/tipo de contenido para mostrar en pestañas.
    Los permisos de autenticación y núcleo se agrupan juntos, otros módulos se mantienen separados.
    
    Returns:
        dict: Diccionario con permisos agrupados por módulo
    """
    permissions = Permission.objects.select_related('content_type').all()
    
    # Agrupar permisos por content_type
    permissions_by_module = {}
    
    # Diccionario de traducciones de módulos
    module_translations = {
        'admin': 'Administración',
        'auth': 'Autenticación',
        'contenttypes': 'Tipos de Contenido',
        'sessions': 'Sesiones',
        'core': 'Núcleo',
        'users': 'Usuarios',
        'alumnos': 'Alumnos',
        'docentes': 'Docentes',
        'asistencia': 'Asistencia',
        'workcenter': 'Centro de Trabajo'
    }
    
    # Diccionario de traducciones de modelos
    model_translations = {
        # Admin
        'logentry': 'Entrada de Log',
        
        # Auth
        'group': 'Grupo',
        'permission': 'Permiso',
        'user': 'Usuario',
        
        # Contenttypes
        'contenttype': 'Tipo de Contenido',
        
        # Sessions
        'session': 'Sesión',
        
        # Core
        'carrera': 'Carrera',
        'userprofile': 'Perfil de Usuario',
        'materia': 'Materia',
        'docente': 'Docente',
        'curso': 'Curso',
        'alumno': 'Alumno',
        'matricula': 'Matrícula',
        
        # Users
        'role': 'Rol',
        
        # Alumnos
        'alumno': 'Alumno',
        
        # Docentes
        'docente': 'Docente',
        
        # Asistencia
        'asistencia': 'Asistencia',
        
        # Workcenter
        'schoolcycle': 'Ciclo Escolar',
        'workcenter': 'Centro de Trabajo',
        'schoolperiod': 'Período Escolar',
        'classroom': 'Aula',
        'schoolcycleconfig': 'Configuración de Ciclo'
    }
    
    for permission in permissions:
        content_type = permission.content_type
        app_label = content_type.app_label
        model_name = content_type.model
        
        # Crear nombre legible del módulo en español
        module_name = module_translations.get(app_label, app_label.replace('_', ' ').title())
        
        # Crear nombre legible del modelo en español
        model_display_name = model_translations.get(model_name, model_name.replace('_', ' ').title())
        
        # Lógica de agrupación: autenticación, núcleo y workcenter se agrupan, otros se mantienen separados
        if app_label == 'auth':
            # Agrupar todos los permisos de autenticación juntos
            module_key = 'auth_combined'
            module_name = 'Autenticación'
            model_display_name = 'Grupo, Permiso, Usuario'
        elif app_label == 'core':
            # Agrupar todos los permisos del núcleo juntos
            module_key = 'core_combined'
            module_name = 'Núcleo'
            model_display_name = 'Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula'
        elif app_label == 'workcenter':
            # Agrupar todos los permisos de workcenter juntos
            module_key = 'workcenter_combined'
            module_name = 'Centro de Trabajo'
            model_display_name = 'Aula, Ciclo Escolar, Configuración de Ciclo, Período Escolar, Centro de Trabajo'
        elif app_label == 'users':
            # Agrupar todos los permisos de users juntos
            module_key = 'users_combined'
            module_name = 'Usuarios'
            model_display_name = 'Rol, Usuario'
        else:
            # Mantener otros módulos separados por modelo
            module_key = f"{app_label}_{model_name}"
        
        if module_key not in permissions_by_module:
            permissions_by_module[module_key] = {
                'module_name': module_name,
                'model_name': model_display_name,
                'app_label': app_label,
                'content_type': content_type,
                'permissions': []
            }
        
        permissions_by_module[module_key]['permissions'].append(permission)
    
    # Ordenar por nombre del módulo
    return dict(sorted(permissions_by_module.items(), key=lambda x: x[1]['module_name']))

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
    
    # Obtener permisos agrupados por módulo
    permissions_by_module = get_permissions_by_module()
    
    return render(request, 'users/role_form.html', {
        'form': form,
        'title': 'Crear Rol',
        'permissions_by_module': permissions_by_module
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
    
    # Obtener permisos agrupados por módulo
    permissions_by_module = get_permissions_by_module()
    
    return render(request, 'users/role_form.html', {
        'form': form,
        'title': 'Actualizar Rol',
        'role': role,
        'permissions_by_module': permissions_by_module
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
