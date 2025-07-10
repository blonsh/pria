from django.contrib import admin
from .models import UserProfile, Carrera, Materia, Docente, Alumno, Curso, Matricula, EducationalLevel, AcademicProgram, Catalogo, CatalogoItem, Genero, ActivityLog

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_login_ip', 'last_activity')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_filter = ('last_activity',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion_anios', 'activa')
    list_filter = ('activa', 'duracion_anios')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos')
    list_filter = ('creditos',)
    search_fields = ('codigo', 'nombre')
    ordering = ('codigo',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad', 'fecha_contratacion')
    list_filter = ('especialidad', 'fecha_contratacion')
    search_fields = ('user__first_name', 'user__last_name', 'especialidad')
    ordering = ('user__last_name', 'user__first_name')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento', 'carrera')
    list_filter = ('fecha_nacimiento', 'carrera')
    search_fields = ('user__first_name', 'user__last_name')
    ordering = ('user__last_name', 'user__first_name')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('materia', 'docente', 'anio_academico', 'semestre', 'cupo_maximo')
    list_filter = ('anio_academico', 'semestre', 'materia')
    search_fields = ('materia__nombre', 'docente__user__first_name', 'docente__user__last_name')
    ordering = ('anio_academico', 'semestre', 'materia__codigo')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'fecha_matricula')
    list_filter = ('fecha_matricula', 'curso__anio_academico', 'curso__semestre')
    search_fields = ('alumno__user__first_name', 'alumno__user__last_name', 'curso__materia__nombre')
    ordering = ('-fecha_matricula',)

@admin.register(EducationalLevel)
class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo', 'es_nivel_superior')
    list_filter = ('activo', 'es_nivel_superior')
    search_fields = ('nombre',)
    ordering = ('orden', 'nombre')
    list_editable = ('orden', 'activo')

@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel_educativo', 'duracion', 'es_temporal', 'activo')
    list_filter = ('nivel_educativo', 'es_temporal', 'activo')
    search_fields = ('nombre', 'descripcion', 'nivel_educativo__nombre')
    ordering = ('nivel_educativo__orden', 'nombre')
    list_editable = ('activo',)
    autocomplete_fields = ['nivel_educativo']

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    list_editable = ('activo',)

@admin.register(CatalogoItem)
class CatalogoItemAdmin(admin.ModelAdmin):
    list_display = ('catalogo', 'valor', 'descripcion', 'orden', 'activo')
    list_filter = ('catalogo', 'activo')
    search_fields = ('valor', 'descripcion', 'catalogo__nombre')
    ordering = ('catalogo', 'orden', 'valor')
    list_editable = ('orden', 'activo')
    autocomplete_fields = ['catalogo']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'orden', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('orden', 'nombre')
    list_editable = ('orden', 'activo')

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'module', 'object_type', 'timestamp', 'ip_address')
    list_filter = ('action', 'module', 'timestamp', 'user')
    search_fields = ('user__username', 'description', 'object_name', 'ip_address')
    readonly_fields = ('user', 'action', 'module', 'object_type', 'object_id', 'object_name',
                      'description', 'ip_address', 'user_agent', 'timestamp', 'additional_data')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser 