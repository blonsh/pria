from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(_('nombre'), max_length=50, unique=True)
    description = models.TextField(_('descripción'), blank=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permisos'),
        blank=True,
        related_name='roles'
    )
    
    class Meta:
        verbose_name = _('rol')
        verbose_name_plural = _('roles')
        
    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(
        Role,
        verbose_name=_('rol'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_permissions(self):
        """Obtener todos los permisos del usuario"""
        if self.is_superuser:
            return Permission.objects.all()
        return Permission.objects.filter(
            models.Q(group__user=self) | 
            models.Q(role__permissions=models.F('id'))
        ).distinct()
