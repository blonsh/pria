from django.urls import path
from . import views

app_name = 'planes_estudio'

urlpatterns = [
    # Dashboard
    path('', views.dashboard_planes_estudio, name='dashboard'),
    
    # Documentación
    path('documentacion/', views.documentacion_view, name='documentacion'),
    
    # Planes de estudios
    path('planes/', views.PlanEstudioListView.as_view(), name='plan_list'),
    path('planes/crear/', views.PlanEstudioCreateView.as_view(), name='plan_create'),
    path('planes/<int:pk>/', views.PlanEstudioDetailView.as_view(), name='plan_detail'),
    path('planes/<int:pk>/editar/', views.PlanEstudioUpdateView.as_view(), name='plan_update'),
    path('planes/<int:pk>/eliminar/', views.PlanEstudioDeleteView.as_view(), name='plan_delete'),
    
    # Semestres
    path('planes/<int:plan_id>/semestres/', views.semestre_list, name='semestre_list'),
    path('planes/<int:plan_id>/semestres/crear/', views.semestre_create, name='semestre_create'),
    path('planes/<int:plan_id>/semestres/<int:semestre_id>/editar/', views.semestre_update, name='semestre_update'),
    
    # Materias
    path('planes/<int:plan_id>/semestres/<int:semestre_id>/materias/', views.materia_list, name='materia_list'),
    path('planes/<int:plan_id>/semestres/<int:semestre_id>/materias/crear/', views.materia_create, name='materia_create'),
    path('planes/<int:plan_id>/semestres/<int:semestre_id>/materias/<int:materia_id>/editar/', views.materia_update, name='materia_update'),
    
    # Competencias
    path('competencias/', views.CompetenciaListView.as_view(), name='competencia_list'),
    path('competencias/crear/', views.CompetenciaCreateView.as_view(), name='competencia_create'),
    
    # Objetivos educativos
    path('planes/<int:plan_id>/objetivos/', views.objetivo_list, name='objetivo_list'),
    path('planes/<int:plan_id>/objetivos/crear/', views.objetivo_create, name='objetivo_create'),
    
    # Perfil de egreso
    path('planes/<int:plan_id>/perfil-egreso/', views.perfil_egreso_detail, name='perfil_egreso_detail'),
    
    # Vistas AJAX
    path('ajax/materias-por-carrera/', views.get_materias_by_carrera, name='get_materias_by_carrera'),
    path('ajax/semestres-por-plan/', views.get_semestres_by_plan, name='get_semestres_by_plan'),
] 