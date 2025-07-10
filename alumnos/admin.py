from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero_cuenta', 'programa_academico')
    list_filter = ('programa_academico', 'work_center', 'genero')
    search_fields = ('user__first_name', 'user__last_name', 'numero_cuenta')
    ordering = ['user__last_name', 'user__first_name']
