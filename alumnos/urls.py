from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    # Dashboard
    path('', views.alumno_dashboard, name='dashboard'),
    
    # CRUD de alumnos
    path('list/', views.alumno_list, name='alumno_list'),
    path('create/', views.alumno_create, name='alumno_create'),
    path('<int:pk>/', views.alumno_detail, name='alumno_detail'),
    path('<int:pk>/edit/', views.alumno_update, name='alumno_update'),
    path('<int:pk>/delete/', views.alumno_delete, name='alumno_delete'),
] 