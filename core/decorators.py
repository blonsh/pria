from functools import wraps
from django.shortcuts import redirect
from core.utils import UserRoles

def role_required(role):
    """
    Decorador que verifica si el usuario tiene el rol requerido.
    
    Args:
        role (str): El rol requerido (admin, docente, alumno)
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect('login')
            
            if role == UserRoles.ADMIN and not UserRoles.is_admin(user):
                return redirect('home')
            elif role == UserRoles.DOCENTE and not UserRoles.is_docente(user):
                return redirect('home')
            elif role == UserRoles.ALUMNO and not UserRoles.is_alumno(user):
                return redirect('home')
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
