from django.db import models
from django.utils.translation import gettext_lazy as _

class WorkCenter(models.Model):
    name = models.CharField(_('nombre'), max_length=100)
    address = models.TextField(_('dirección'))
    director_name = models.CharField(_('nombre del director'), max_length=100)
    school_control_name = models.CharField(_('nombre del control escolar'), max_length=100)
    
    class Meta:
        verbose_name = _('centro de trabajo')
        verbose_name_plural = _('centros de trabajo')
        
    def __str__(self):
        return self.name

class Classroom(models.Model):
    work_center = models.ForeignKey(
        WorkCenter,
        verbose_name=_('centro de trabajo'),
        on_delete=models.CASCADE
    )
    name = models.CharField(_('nombre'), max_length=50)
    capacity = models.PositiveIntegerField(_('capacidad'), default=30)
    
    class Meta:
        verbose_name = _('aula')
        verbose_name_plural = _('aulas')
        
    def __str__(self):
        return f"{self.name} - {self.work_center.name}"

class SchoolCycle(models.Model):
    work_center = models.ForeignKey(
        WorkCenter,
        verbose_name=_('centro de trabajo'),
        on_delete=models.CASCADE
    )
    name = models.CharField(_('nombre'), max_length=50)
    start_date = models.DateField(_('fecha de inicio'))
    end_date = models.DateField(_('fecha de fin'))
    is_active = models.BooleanField(_('activo'), default=False, help_text=_('Indica si este ciclo está activo'))
    
    class Meta:
        verbose_name = _('ciclo escolar')
        verbose_name_plural = _('ciclos escolares')
        
    def __str__(self):
        return self.name
    
    def is_currently_active(self):
        """Verifica si el ciclo está actualmente activo basado en las fechas"""
        from datetime import date
        today = date.today()
        return self.start_date <= today <= self.end_date

class SchoolCycleConfig(models.Model):
    """Configuración para gestionar ciclos activos por centro de trabajo"""
    work_center = models.OneToOneField(
        WorkCenter,
        verbose_name=_('centro de trabajo'),
        on_delete=models.CASCADE,
        related_name='cycle_config'
    )
    allow_multiple_active = models.BooleanField(
        _('permitir múltiples ciclos activos'),
        default=False,
        help_text=_('Permite tener múltiples ciclos activos simultáneamente')
    )
    auto_activate_by_date = models.BooleanField(
        _('activación automática por fecha'),
        default=True,
        help_text=_('Activa automáticamente los ciclos según las fechas')
    )
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = _('configuración de ciclos')
        verbose_name_plural = _('configuraciones de ciclos')
        
    def __str__(self):
        return f"Configuración - {self.work_center.name}"
    
    def get_active_cycles(self):
        """Obtiene los ciclos activos para este centro de trabajo"""
        if self.auto_activate_by_date:
            from datetime import date
            today = date.today()
            return SchoolCycle.objects.filter(
                work_center=self.work_center,
                start_date__lte=today,
                end_date__gte=today
            )
        else:
            return SchoolCycle.objects.filter(
                work_center=self.work_center,
                is_active=True
            )

class SchoolPeriod(models.Model):
    PERIOD_TYPES = [
        ('BIMESTER', _('Bimestre')),
        ('TRIMESTER', _('Trimestre')),
        ('SEMESTER', _('Semestre')),
        ('ANNUAL', _('Anual')),
    ]
    
    school_cycle = models.ForeignKey(
        SchoolCycle,
        verbose_name=_('ciclo escolar'),
        on_delete=models.CASCADE
    )
    name = models.CharField(_('nombre'), max_length=50)
    period_type = models.CharField(
        _('tipo de período'),
        max_length=10,
        choices=PERIOD_TYPES
    )
    start_date = models.DateField(_('fecha de inicio'))
    end_date = models.DateField(_('fecha de fin'))
    
    class Meta:
        verbose_name = _('periodo escolar')
        verbose_name_plural = _('periodos escolares')
        
    def __str__(self):
        return f"{self.name} - {self.period_type}"
