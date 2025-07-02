from django.contrib import admin
from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad', 'fecha_contratacion')
    list_filter = ('especialidad',)
    search_fields = ('user__first_name', 'user__last_name')
    ordering = ['user__last_name', 'user__first_name']
