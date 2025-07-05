from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Docente(models.Model):
    """
    Modelo que representa un docente.
    """
    user = models.OneToOneField(
        User,
        verbose_name=_('usuario'),
        on_delete=models.CASCADE,
        related_name='docentes_docente'
    )
    especialidad = models.CharField(_('especialidad'), max_length=255)
    fecha_contratacion = models.DateField(_('fecha de contratación'))
    foto = models.ImageField(_('foto'), upload_to='docentes/fotos/', null=True, blank=True)
    
    class Meta:
        verbose_name = _('docente')
        verbose_name_plural = _('docentes')
        ordering = ['user__last_name', 'user__first_name']
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
