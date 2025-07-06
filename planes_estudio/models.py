from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from workcenter.models import WorkCenter, SchoolCycle
from core.models import Carrera, Materia


class PlanEstudio(models.Model):
    """
    Modelo que representa un plan de estudios completo.
    """
    ESTADO_CHOICES = [
        ('BORRADOR', _('Borrador')),
        ('ACTIVO', _('Activo')),
        ('INACTIVO', _('Inactivo')),
        ('ARCHIVADO', _('Archivado')),
    ]
    
    nombre = models.CharField(_('nombre'), max_length=255)
    descripcion = models.TextField(_('descripción'), blank=True)
    carrera = models.ForeignKey(
        Carrera,
        verbose_name=_('carrera'),
        on_delete=models.CASCADE,
        related_name='planes_estudio'
    )
    work_center = models.ForeignKey(
        WorkCenter,
        verbose_name=_('centro de trabajo'),
        on_delete=models.CASCADE,
        related_name='planes_estudio'
    )
    ciclo_inicio = models.ForeignKey(
        SchoolCycle,
        verbose_name=_('ciclo de inicio'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='planes_inicio'
    )
    duracion_semestres = models.PositiveIntegerField(
        _('duración en semestres'),
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    creditos_totales = models.PositiveIntegerField(
        _('créditos totales'),
        validators=[MinValueValidator(1)]
    )
    estado = models.CharField(
        _('estado'),
        max_length=20,
        choices=ESTADO_CHOICES,
        default='BORRADOR'
    )
    fecha_creacion = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    creado_por = models.ForeignKey(
        'auth.User',
        verbose_name=_('creado por'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = _('plan de estudios')
        verbose_name_plural = _('planes de estudios')
        unique_together = ['carrera', 'work_center', 'nombre']
        
    def __str__(self):
        return f"{self.nombre} - {self.carrera.nombre}"
    
    def get_semestres_count(self):
        """Retorna el número de semestres configurados"""
        return self.semestres.count()
    
    def get_creditos_actuales(self):
        """Calcula los créditos totales actuales del plan"""
        return sum(semestre.get_creditos_semestre() for semestre in self.semestres.all())


class SemestrePlan(models.Model):
    """
    Modelo que representa un semestre dentro de un plan de estudios.
    """
    plan_estudio = models.ForeignKey(
        PlanEstudio,
        verbose_name=_('plan de estudios'),
        on_delete=models.CASCADE,
        related_name='semestres'
    )
    numero_semestre = models.PositiveIntegerField(
        _('número de semestre'),
        validators=[MinValueValidator(1)]
    )
    nombre = models.CharField(_('nombre'), max_length=100, blank=True)
    creditos_semestre = models.PositiveIntegerField(
        _('créditos del semestre'),
        default=0
    )
    es_optativo = models.BooleanField(_('es optativo'), default=False)
    descripcion = models.TextField(_('descripción'), blank=True)
    
    class Meta:
        verbose_name = _('semestre del plan')
        verbose_name_plural = _('semestres del plan')
        unique_together = ['plan_estudio', 'numero_semestre']
        ordering = ['numero_semestre']
        
    def __str__(self):
        return f"Semestre {self.numero_semestre} - {self.plan_estudio.nombre}"
    
    def get_creditos_semestre(self):
        """Calcula los créditos totales del semestre"""
        return sum(materia.creditos for materia in self.materias.all())
    
    def save(self, *args, **kwargs):
        # Actualizar créditos del semestre automáticamente
        super().save(*args, **kwargs)
        self.creditos_semestre = self.get_creditos_semestre()
        if self.pk:  # Solo si ya existe
            super().save(update_fields=['creditos_semestre'])


class MateriaPlan(models.Model):
    """
    Modelo que representa una materia dentro de un semestre del plan de estudios.
    """
    TIPO_MATERIA_CHOICES = [
        ('OBLIGATORIA', _('Obligatoria')),
        ('OPTATIVA', _('Optativa')),
        ('COMPLEMENTARIA', _('Complementaria')),
    ]
    
    semestre = models.ForeignKey(
        SemestrePlan,
        verbose_name=_('semestre'),
        on_delete=models.CASCADE,
        related_name='materias'
    )
    materia = models.ForeignKey(
        Materia,
        verbose_name=_('materia'),
        on_delete=models.CASCADE
    )
    tipo_materia = models.CharField(
        _('tipo de materia'),
        max_length=20,
        choices=TIPO_MATERIA_CHOICES,
        default='OBLIGATORIA'
    )
    creditos = models.PositiveIntegerField(
        _('créditos'),
        validators=[MinValueValidator(1)]
    )
    horas_teoria = models.PositiveIntegerField(
        _('horas de teoría'),
        default=0
    )
    horas_practica = models.PositiveIntegerField(
        _('horas de práctica'),
        default=0
    )
    horas_independiente = models.PositiveIntegerField(
        _('horas independiente'),
        default=0
    )
    prerequisitos = models.ManyToManyField(
        'self',
        verbose_name=_('prerrequisitos'),
        blank=True,
        symmetrical=False
    )
    orden = models.PositiveIntegerField(
        _('orden'),
        default=1,
        help_text=_('Orden de la materia dentro del semestre')
    )
    
    class Meta:
        verbose_name = _('materia del plan')
        verbose_name_plural = _('materias del plan')
        unique_together = ['semestre', 'materia']
        ordering = ['orden']
        
    def __str__(self):
        return f"{self.materia.nombre} - Semestre {self.semestre.numero_semestre}"
    
    def get_horas_totales(self):
        """Calcula las horas totales de la materia"""
        return self.horas_teoria + self.horas_practica + self.horas_independiente


class Competencia(models.Model):
    """
    Modelo que representa las competencias que desarrolla una materia.
    """
    TIPO_COMPETENCIA_CHOICES = [
        ('GENERICA', _('Genérica')),
        ('ESPECIFICA', _('Específica')),
        ('TRANSVERSAL', _('Transversal')),
    ]
    
    nombre = models.CharField(_('nombre'), max_length=255)
    descripcion = models.TextField(_('descripción'))
    tipo_competencia = models.CharField(
        _('tipo de competencia'),
        max_length=20,
        choices=TIPO_COMPETENCIA_CHOICES,
        default='ESPECIFICA'
    )
    materias = models.ManyToManyField(
        MateriaPlan,
        verbose_name=_('materias'),
        related_name='competencias',
        blank=True
    )
    
    class Meta:
        verbose_name = _('competencia')
        verbose_name_plural = _('competencias')
        
    def __str__(self):
        return self.nombre


class ObjetivoEducativo(models.Model):
    """
    Modelo que representa los objetivos educativos de un plan de estudios.
    """
    plan_estudio = models.ForeignKey(
        PlanEstudio,
        verbose_name=_('plan de estudios'),
        on_delete=models.CASCADE,
        related_name='objetivos_educativos'
    )
    titulo = models.CharField(_('título'), max_length=255)
    descripcion = models.TextField(_('descripción'))
    orden = models.PositiveIntegerField(_('orden'), default=1)
    
    class Meta:
        verbose_name = _('objetivo educativo')
        verbose_name_plural = _('objetivos educativos')
        ordering = ['orden']
        
    def __str__(self):
        return self.titulo


class PerfilEgreso(models.Model):
    """
    Modelo que representa el perfil de egreso de un plan de estudios.
    """
    plan_estudio = models.OneToOneField(
        PlanEstudio,
        verbose_name=_('plan de estudios'),
        on_delete=models.CASCADE,
        related_name='perfil_egreso'
    )
    descripcion_general = models.TextField(_('descripción general'))
    competencias_generales = models.TextField(_('competencias generales'))
    competencias_especificas = models.TextField(_('competencias específicas'))
    campo_laboral = models.TextField(_('campo laboral'))
    fecha_actualizacion = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = _('perfil de egreso')
        verbose_name_plural = _('perfiles de egreso')
        
    def __str__(self):
        return f"Perfil de egreso - {self.plan_estudio.nombre}"


class VersionPlanEstudio(models.Model):
    """
    Modelo para versionar los planes de estudios.
    """
    plan_estudio = models.ForeignKey(
        PlanEstudio,
        verbose_name=_('plan de estudios'),
        on_delete=models.CASCADE,
        related_name='versiones'
    )
    numero_version = models.PositiveIntegerField(_('número de versión'))
    fecha_creacion = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    cambios_descripcion = models.TextField(_('descripción de cambios'), blank=True)
    creado_por = models.ForeignKey(
        'auth.User',
        verbose_name=_('creado por'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    es_activa = models.BooleanField(_('es activa'), default=True)
    
    class Meta:
        verbose_name = _('versión del plan')
        verbose_name_plural = _('versiones del plan')
        unique_together = ['plan_estudio', 'numero_version']
        ordering = ['-numero_version']
        
    def __str__(self):
        return f"Versión {self.numero_version} - {self.plan_estudio.nombre}"
