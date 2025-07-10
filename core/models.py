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
        on_delete=models.CASCADE,
        related_name='core_alumno'
    )
    fecha_nacimiento = models.DateField(_('fecha de nacimiento'))
    carrera = models.ForeignKey(
        Carrera,
        verbose_name=_('carrera'),
        on_delete=models.SET_NULL,
        related_name='core_alumnos',
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

class EducationalLevel(models.Model):
    """
    Modelo que representa niveles educativos: Maternal, Preescolar, Primaria, etc.
    """
    nombre = models.CharField(_('nombre'), max_length=100)
    orden = models.IntegerField(_('orden'), default=0, help_text=_("Para ordenar en listas"))
    activo = models.BooleanField(_('activo'), default=True)
    es_nivel_superior = models.BooleanField(_('es nivel superior'), default=False, 
                                          help_text=_("Para diferenciar niveles universitarios"))
    
    class Meta:
        verbose_name = _('nivel educativo')
        verbose_name_plural = _('niveles educativos')
        ordering = ['orden', 'nombre']
        
    def __str__(self):
        return self.nombre

class AcademicProgram(models.Model):
    """
    Modelo que representa programas académicos flexibles para cualquier nivel educativo.
    """
    nombre = models.CharField(_('nombre'), max_length=150)
    nivel_educativo = models.ForeignKey(
        EducationalLevel,
        verbose_name=_('nivel educativo'),
        on_delete=models.PROTECT,
        related_name='programas'
    )
    descripcion = models.TextField(_('descripción'), blank=True, null=True)
    duracion = models.CharField(_('duración'), max_length=50, blank=True, 
                               help_text=_("Ejemplo: '3 años', '1 semestre', '4 semanas'"))
    es_temporal = models.BooleanField(_('es temporal'), default=False, 
                                    help_text=_("¿Es un curso temporal como un curso de verano?"))
    activo = models.BooleanField(_('activo'), default=True)
    
    class Meta:
        verbose_name = _('programa académico')
        verbose_name_plural = _('programas académicos')
        unique_together = ('nombre', 'nivel_educativo')
        ordering = ['nivel_educativo__orden', 'nombre']
        
    def __str__(self):
        return f"{self.nombre} ({self.nivel_educativo.nombre})"

# Agregando tipos de usuario a User
User.add_to_class('TIPO_DOCENTE', 'docente')
User.add_to_class('TIPO_ALUMNO', 'alumno')
User.add_to_class('TIPO_ADMIN', 'admin')

class Catalogo(models.Model):
    """
    Modelo que representa un catálogo de datos.
    Permite crear listas de valores para diferentes campos del sistema.
    """
    nombre = models.CharField(_('nombre'), max_length=100, unique=True)
    descripcion = models.TextField(_('descripción'), blank=True)
    activo = models.BooleanField(_('activo'), default=True)
    fecha_creacion = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    
    class Meta:
        verbose_name = _('catálogo')
        verbose_name_plural = _('catálogos')
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class CatalogoItem(models.Model):
    """
    Modelo que representa un elemento de un catálogo.
    """
    catalogo = models.ForeignKey(
        Catalogo,
        verbose_name=_('catálogo'),
        on_delete=models.CASCADE,
        related_name='items'
    )
    valor = models.CharField(_('valor'), max_length=100)
    descripcion = models.CharField(_('descripción'), max_length=255, blank=True)
    orden = models.IntegerField(_('orden'), default=0, help_text=_("Para ordenar en listas"))
    activo = models.BooleanField(_('activo'), default=True)
    
    class Meta:
        verbose_name = _('elemento de catálogo')
        verbose_name_plural = _('elementos de catálogo')
        unique_together = ('catalogo', 'valor')
        ordering = ['catalogo', 'orden', 'valor']
        
    def __str__(self):
        return f"{self.catalogo.nombre}: {self.valor}"

class Genero(models.Model):
    """
    Modelo que representa los géneros disponibles.
    """
    nombre = models.CharField(_('nombre'), max_length=50, unique=True)
    descripcion = models.CharField(_('descripción'), max_length=255, blank=True)
    activo = models.BooleanField(_('activo'), default=True)
    orden = models.IntegerField(_('orden'), default=0)
    
    class Meta:
        verbose_name = _('género')
        verbose_name_plural = _('géneros')
        ordering = ['orden', 'nombre']
        
    def __str__(self):
        return self.nombre

class ActivityLog(models.Model):
    """
    Modelo para registrar todas las actividades de los usuarios en el sistema.
    """
    ACTION_CHOICES = [
        ('CREATE', 'Crear'),
        ('UPDATE', 'Actualizar'),
        ('DELETE', 'Eliminar'),
        ('LOGIN', 'Iniciar Sesión'),
        ('LOGOUT', 'Cerrar Sesión'),
        ('VIEW', 'Ver'),
        ('EXPORT', 'Exportar'),
        ('IMPORT', 'Importar'),
        ('DOWNLOAD', 'Descargar'),
        ('UPLOAD', 'Subir'),
        ('APPROVE', 'Aprobar'),
        ('REJECT', 'Rechazar'),
        ('ASSIGN', 'Asignar'),
        ('UNASSIGN', 'Desasignar'),
    ]
    
    MODULE_CHOICES = [
        ('USERS', 'Usuarios'),
        ('ALUMNOS', 'Alumnos'),
        ('DOCENTES', 'Docentes'),
        ('ASISTENCIA', 'Asistencia'),
        ('PLANES_ESTUDIO', 'Planes de Estudio'),
        ('WORKCENTER', 'Centro de Trabajo'),
        ('MATRICULAS', 'Matrículas'),
        ('REPORTES', 'Reportes'),
        ('CONTROL_ESCOLAR', 'Control Escolar'),
        ('SYSTEM', 'Sistema'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, verbose_name='Acción')
    module = models.CharField(max_length=20, choices=MODULE_CHOICES, verbose_name='Módulo')
    object_type = models.CharField(max_length=100, verbose_name='Tipo de Objeto')
    object_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='ID del Objeto')
    object_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre del Objeto')
    description = models.TextField(verbose_name='Descripción')
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name='Dirección IP')
    user_agent = models.TextField(blank=True, null=True, verbose_name='User Agent')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')
    additional_data = models.JSONField(blank=True, null=True, verbose_name='Datos Adicionales')
    
    class Meta:
        verbose_name = 'Log de Actividad'
        verbose_name_plural = 'Logs de Actividades'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', 'timestamp']),
            models.Index(fields=['action', 'timestamp']),
            models.Index(fields=['module', 'timestamp']),
            models.Index(fields=['timestamp']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} - {self.get_module_display()} - {self.timestamp}"
    
    @classmethod
    def log_activity(cls, user, action, module, object_type, description, 
                     object_id=None, object_name=None, ip_address=None, 
                     user_agent=None, additional_data=None):
        """
        Método de clase para registrar una actividad de forma fácil.
        """
        return cls.objects.create(
            user=user,
            action=action,
            module=module,
            object_type=object_type,
            object_id=object_id,
            object_name=object_name,
            description=description,
            ip_address=ip_address,
            user_agent=user_agent,
            additional_data=additional_data
        )
