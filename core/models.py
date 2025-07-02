from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    """
    Modelo que extiende la información del usuario.
    Permite almacenar datos adicionales relacionados con el usuario.
    """
    user = models.OneToOneField(
        User,
        verbose_name=_('usuario'),
        on_delete=models.CASCADE
    )
    last_login_ip = models.GenericIPAddressField(
        _('última IP'),
        null=True,
        blank=True
    )
    last_activity = models.DateTimeField(
        _('última actividad'),
        auto_now=True
    )
    
    class Meta:
        verbose_name = _('perfil de usuario')
        verbose_name_plural = _('perfiles de usuario')
        
    def __str__(self):
        return f"Perfil de {self.user.username}"

class Carrera(models.Model):
    """
    Modelo que representa una carrera académica.
    """
    nombre = models.CharField(_('nombre'), max_length=255)
    descripcion = models.TextField(_('descripción'), blank=True)
    duracion_anios = models.IntegerField(_('duración en años'))
    activa = models.BooleanField(_('activa'), default=True)
    
    class Meta:
        verbose_name = _('carrera')
        verbose_name_plural = _('carreras')
        
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    """
    Modelo que representa una materia académica.
    """
    nombre = models.CharField(_('nombre'), max_length=255)
    codigo = models.CharField(_('código'), max_length=20, unique=True)
    creditos = models.IntegerField(_('créditos'))
    carrera = models.ManyToManyField(
        Carrera,
        verbose_name=_('carreras'),
        related_name='materias'
    )
    
    class Meta:
        verbose_name = _('materia')
        verbose_name_plural = _('materias')
        
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Docente(models.Model):
    """
    Modelo que representa un docente.
    """
    user = models.OneToOneField(
        User,
        verbose_name=_('usuario'),
        on_delete=models.CASCADE
    )
    especialidad = models.CharField(_('especialidad'), max_length=255)
    fecha_contratacion = models.DateField(_('fecha de contratación'))
    
    class Meta:
        verbose_name = _('docente')
        verbose_name_plural = _('docentes')
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

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
        Carrera,
        verbose_name=_('carrera'),
        on_delete=models.SET_NULL,
        null=True
    )
    
    class Meta:
        verbose_name = _('alumno')
        verbose_name_plural = _('alumnos')
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Curso(models.Model):
    """
    Modelo que representa un curso específico de una materia.
    """
    materia = models.ForeignKey(
        Materia,
        verbose_name=_('materia'),
        on_delete=models.CASCADE
    )
    docente = models.ForeignKey(
        Docente,
        verbose_name=_('docente'),
        on_delete=models.SET_NULL,
        null=True
    )
    anio_academico = models.IntegerField(_('año académico'))
    semestre = models.IntegerField(_('semestre'), choices=[(1, 'Primero'), (2, 'Segundo')])
    cupo_maximo = models.IntegerField(_('cupo máximo'))
    
    class Meta:
        verbose_name = _('curso')
        verbose_name_plural = _('cursos')
        unique_together = ['materia', 'anio_academico', 'semestre']
        
    def __str__(self):
        return f"{self.materia.codigo} - {self.materia.nombre} ({self.anio_academico}-{self.semestre})"

class Matricula(models.Model):
    """
    Modelo que representa la matrícula de un alumno en un curso.
    """
    alumno = models.ForeignKey(
        Alumno,
        verbose_name=_('alumno'),
        on_delete=models.CASCADE
    )
    curso = models.ForeignKey(
        Curso,
        verbose_name=_('curso'),
        on_delete=models.CASCADE
    )
    fecha_matricula = models.DateField(_('fecha de matrícula'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('matrícula')
        verbose_name_plural = _('matrículas')
        unique_together = ['alumno', 'curso']
        
    def __str__(self):
        return f"{self.alumno.user.first_name} {self.alumno.user.last_name} - {self.curso}"

# Agregando tipos de usuario a User
User.add_to_class('TIPO_DOCENTE', 'docente')
User.add_to_class('TIPO_ALUMNO', 'alumno')
User.add_to_class('TIPO_ADMIN', 'admin')
