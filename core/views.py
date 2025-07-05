from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from core.decorators import role_required
from core.utils import UserRoles
from core.forms import UserRegistrationForm, AlumnoRegistrationForm, DocenteRegistrationForm
from django.contrib.auth.models import Group

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
    """Página principal."""
    context = {
        'alumnos_count': 0,  # TODO: Implementar cuando los modelos estén disponibles
        'docentes_count': 0,  # TODO: Implementar cuando los modelos estén disponibles
        'carreras_count': 0   # TODO: Implementar cuando los modelos estén disponibles
    }
    return render(request, 'core/home.html', context)

@login_required
@role_required(UserRoles.ADMIN)
def register_user(request):
    """Vista para registrar un nuevo usuario."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, _('Usuario registrado exitosamente'))
            return redirect('core:home')
        else:
            messages.error(request, _('Error al registrar usuario'))
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'core/register_user.html', {
        'user_form': user_form,
    })

@login_required
@role_required(UserRoles.ADMIN)
def register_alumno(request):
    """Vista para registrar un nuevo alumno."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        alumno_form = AlumnoRegistrationForm(request.POST)
        if user_form.is_valid() and alumno_form.is_valid():
            user = user_form.save()
            alumno = alumno_form.save(commit=False)
            alumno.user = user
            alumno.save()
            messages.success(request, _('Alumno registrado exitosamente'))
            return redirect('core:home')
        else:
            messages.error(request, _('Error al registrar alumno'))
    else:
        user_form = UserRegistrationForm()
        alumno_form = AlumnoRegistrationForm()
    
    return render(request, 'core/register_alumno.html', {
        'user_form': user_form,
        'alumno_form': alumno_form,
    })

@login_required
@role_required(UserRoles.ADMIN)
def register_docente(request):
    """Vista para registrar un nuevo docente."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        docente_form = DocenteRegistrationForm(request.POST)
        if user_form.is_valid() and docente_form.is_valid():
            user = user_form.save()
            docente = docente_form.save(commit=False)
            docente.user = user
            docente.save()
            messages.success(request, _('Docente registrado exitosamente'))
            return redirect('core:home')
        else:
            messages.error(request, _('Error al registrar docente'))
    else:
        user_form = UserRegistrationForm()
        docente_form = DocenteRegistrationForm()
    
    return render(request, 'core/register_docente.html', {
        'user_form': user_form,
        'docente_form': docente_form,
    })
