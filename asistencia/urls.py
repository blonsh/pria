from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('registrar/', views.registrar_asistencia, name='registrar_asistencia'),
    path('historial/', views.historial_asistencia, name='historial_asistencia'),
    path('reporte/', views.reporte_asistencia, name='reporte_asistencia'),
    path('estadisticas/', views.estadisticas_asistencia, name='estadisticas_asistencia'),
    path('actualizar_estado/<int:pk>/', views.actualizar_estado, name='actualizar_estado'),
]
