from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserRoles:
    """
    Clase que maneja los roles de usuario en el sistema.
    """
    ADMIN = 'admin'
    DOCENTE = 'docente'
    ALUMNO = 'alumno'
    
    CHOICES = [
        (ADMIN, _('Administrador')),
        (DOCENTE, _('Docente')),
        (ALUMNO, _('Alumno'))
    ]
    
    @classmethod
    def get_role_display(cls, role):
        """Obtiene el nombre legible del rol."""
        for value, display in cls.CHOICES:
            if value == role:
                return display
        return _('Desconocido')
    
    @classmethod
    def is_admin(cls, user):
        """Verifica si el usuario es administrador."""
        return user.is_superuser
    
    @classmethod
    def is_docente(cls, user):
        """Verifica si el usuario es docente."""
        return hasattr(user, 'docente')
    
    @classmethod
    def is_alumno(cls, user):
        """Verifica si el usuario es alumno."""
        return hasattr(user, 'alumno')
