from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import (
    PlanEstudio, SemestrePlan, MateriaPlan, Competencia,
    ObjetivoEducativo, PerfilEgreso, VersionPlanEstudio
)


@admin.register(PlanEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'carrera', 'work_center', 'duracion_semestres',
        'creditos_totales', 'estado', 'fecha_creacion'
    ]
    list_filter = ['estado', 'carrera', 'work_center', 'fecha_creacion']
    search_fields = ['nombre', 'carrera__nombre', 'work_center__name']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    fieldsets = (
        (_('Información básica'), {
            'fields': ('nombre', 'descripcion', 'carrera', 'work_center')
        }),
        (_('Configuración académica'), {
            'fields': ('duracion_semestres', 'creditos_totales', 'ciclo_inicio')
        }),
        (_('Estado'), {
            'fields': ('estado', 'creado_por')
        }),
        (_('Fechas'), {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('carrera', 'work_center')


@admin.register(SemestrePlan)
class SemestrePlanAdmin(admin.ModelAdmin):
    list_display = [
        'numero_semestre', 'plan_estudio', 'creditos_semestre',
        'es_optativo', 'get_materias_count'
    ]
    list_filter = ['plan_estudio', 'es_optativo']
    search_fields = ['plan_estudio__nombre', 'nombre']
    ordering = ['plan_estudio', 'numero_semestre']
    
    def get_materias_count(self, obj):
        return obj.materias.count()
    get_materias_count.short_description = _('Número de materias')


@admin.register(MateriaPlan)
class MateriaPlanAdmin(admin.ModelAdmin):
    list_display = [
        'materia', 'semestre', 'tipo_materia', 'creditos',
        'get_horas_totales', 'orden'
    ]
    list_filter = ['tipo_materia', 'semestre__plan_estudio', 'semestre']
    search_fields = ['materia__nombre', 'materia__codigo']
    ordering = ['semestre', 'orden']
    filter_horizontal = ['prerequisitos']
    
    def get_horas_totales(self, obj):
        return obj.get_horas_totales()
    get_horas_totales.short_description = _('Horas totales')


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_competencia', 'get_materias_count']
    list_filter = ['tipo_competencia']
    search_fields = ['nombre', 'descripcion']
    filter_horizontal = ['materias']
    
    def get_materias_count(self, obj):
        return obj.materias.count()
    get_materias_count.short_description = _('Número de materias')


@admin.register(ObjetivoEducativo)
class ObjetivoEducativoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'plan_estudio', 'orden']
    list_filter = ['plan_estudio']
    search_fields = ['titulo', 'descripcion']
    ordering = ['plan_estudio', 'orden']


@admin.register(PerfilEgreso)
class PerfilEgresoAdmin(admin.ModelAdmin):
    list_display = ['plan_estudio', 'fecha_actualizacion']
    search_fields = ['plan_estudio__nombre']
    readonly_fields = ['fecha_actualizacion']
    fieldsets = (
        (_('Plan de estudios'), {
            'fields': ('plan_estudio',)
        }),
        (_('Descripción general'), {
            'fields': ('descripcion_general',)
        }),
        (_('Competencias'), {
            'fields': ('competencias_generales', 'competencias_especificas')
        }),
        (_('Campo laboral'), {
            'fields': ('campo_laboral',)
        }),
        (_('Fechas'), {
            'fields': ('fecha_actualizacion',),
            'classes': ('collapse',)
        }),
    )


@admin.register(VersionPlanEstudio)
class VersionPlanEstudioAdmin(admin.ModelAdmin):
    list_display = [
        'plan_estudio', 'numero_version', 'fecha_creacion',
        'es_activa', 'creado_por'
    ]
    list_filter = ['es_activa', 'fecha_creacion', 'plan_estudio']
    search_fields = ['plan_estudio__nombre', 'cambios_descripcion']
    readonly_fields = ['fecha_creacion']
    ordering = ['plan_estudio', '-numero_version']
