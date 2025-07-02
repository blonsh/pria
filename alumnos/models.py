from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Alumno(models.Model):
    """
    Modelo que representa un alumno.
    """
    user = models.OneToOneField(
        User,
        verbose_name=_('usuario'),
        on_delete=models.CASCADE
    )
    fecha_nacimiento = models.DateField(_('fecha de nacimiento'))
    carrera = models.ForeignKey(
        'core.Carrera',
        verbose_name=_('carrera'),
        on_delete=models.SET_NULL,
        null=True
    )
    numero_cuenta = models.CharField(_('número de cuenta'), max_length=20, unique=True)
    foto = models.ImageField(_('foto'), upload_to='alumnos/fotos/', null=True, blank=True)
    
    class Meta:
        verbose_name = _('alumno')
        verbose_name_plural = _('alumnos')
        ordering = ['user__last_name', 'user__first_name']
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class AlumnoAdmin(models.ModelAdmin):
    list_display = ('user', 'numero_cuenta', 'carrera')
    list_filter = ('carrera',)
    search_fields = ('user__first_name', 'user__last_name', 'numero_cuenta')
