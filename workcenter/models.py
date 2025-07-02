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
    
    class Meta:
        verbose_name = _('ciclo escolar')
        verbose_name_plural = _('ciclos escolares')
        
    def __str__(self):
        return self.name

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
