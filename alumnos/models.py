from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models import Max
from datetime import datetime


class Alumno(models.Model):
    """
    Modelo que representa un alumno.
    """
    user = models.OneToOneField(
        User,
        verbose_name=_('usuario'),
        on_delete=models.CASCADE,
        related_name='alumnos_alumno'
    )
    fecha_nacimiento = models.DateField(_('fecha de nacimiento'))
    programa_academico = models.ForeignKey(
        'core.AcademicProgram',
        verbose_name=_('programa académico'),
        on_delete=models.SET_NULL,
        related_name='alumnos',
        null=True,
        blank=True
    )
    work_center = models.ForeignKey(
        'workcenter.WorkCenter',
        verbose_name=_('centro de trabajo'),
        on_delete=models.CASCADE,
        related_name='alumnos',
        null=True,
        blank=True
    )
    numero_cuenta = models.CharField(_('número de cuenta'), max_length=20, unique=True, editable=False)
    foto = models.ImageField(_('foto'), upload_to='alumnos/fotos/', null=True, blank=True)
    
    # Nuevos campos
    curp = models.CharField(_('CURP'), max_length=18, unique=True, blank=True, null=True, help_text=_('Clave Única de Registro de Población'))
    telefono_contacto = models.CharField(_('teléfono de contacto'), max_length=15, blank=True, help_text=_('Número de teléfono para contacto'))
    
    # Datos de contacto de emergencia
    nombre_contacto_emergencia = models.CharField(_('nombre del contacto de emergencia'), max_length=100, blank=True)
    telefono_contacto_emergencia = models.CharField(_('teléfono del contacto de emergencia'), max_length=15, blank=True)
    
    # Campo de género
    genero = models.ForeignKey(
        'core.Genero',
        verbose_name=_('género'),
        on_delete=models.SET_NULL,
        related_name='alumnos',
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = _('alumno')
        verbose_name_plural = _('alumnos')
        ordering = ['user__last_name', 'user__first_name']
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def save(self, *args, **kwargs):
        """Genera automáticamente el número de cuenta."""
        if not self.numero_cuenta:
            self.numero_cuenta = self.generate_numero_cuenta()
        super().save(*args, **kwargs)
    
    def generate_numero_cuenta(self):
        """
        Genera automáticamente el número de cuenta con formato:
        {año_2_dígitos}-{centro_2_dígitos}-{número_secuencial}
        Ejemplo: 24-01-00001
        """
        current_year = datetime.now().year
        year_short = str(current_year)[-2:]  # Solo los últimos 2 dígitos
        
        # Obtener el work_center_id (si no existe, usar 0)
        work_center_id = self.work_center.id if self.work_center else 0
        
        # Formatear el ID del centro de trabajo con 2 dígitos
        work_center_formatted = f"{work_center_id:02d}"
        
        # Buscar el último número secuencial para este work_center y año
        last_numero = Alumno.objects.filter(
            numero_cuenta__startswith=f"{year_short}-{work_center_formatted}-"
        ).aggregate(
            max_numero=Max('numero_cuenta')
        )['max_numero']
        
        if last_numero:
            # Extraer el número secuencial del último número de cuenta
            try:
                last_sequential = int(last_numero.split('-')[-1])
                new_sequential = last_sequential + 1
            except (ValueError, IndexError):
                new_sequential = 1
        else:
            new_sequential = 1
        
        # Formatear el número de cuenta
        numero_cuenta = f"{year_short}-{work_center_formatted}-{new_sequential:05d}"
        
        return numero_cuenta
