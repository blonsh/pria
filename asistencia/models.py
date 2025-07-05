from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from alumnos.models import Alumno
from docentes.models import Docente

class Asistencia(models.Model):
    """Modelo para registrar asistencia"""
    ESTADOS = [
        ('P', _('Presente')),
        ('T', _('Tarde')),
        ('A', _('Ausente')),
    ]
    
    alumno = models.ForeignKey(
        Alumno,
        verbose_name=_('alumno'),
        on_delete=models.CASCADE,
        related_name='asistencias'
    )
    fecha = models.DateField(_('fecha'))
    estado = models.CharField(
        _('estado'),
        max_length=1,
        choices=ESTADOS,
        default='P'
    )
    hora_entrada = models.TimeField(_('hora de entrada'))
    hora_salida = models.TimeField(_('hora de salida'), null=True, blank=True)
    docente = models.ForeignKey(
        Docente,
        verbose_name=_('docente'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='asistencias'
    )
    
    class Meta:
        verbose_name = _('asistencia')
        verbose_name_plural = _('asistencias')
        ordering = ['-fecha', 'alumno__user__last_name']
        
    def __str__(self):
        return f"{self.alumno} - {self.fecha} - {self.get_estado_display()}"
