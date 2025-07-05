from django.urls import path
from . import views

app_name = 'workcenter'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('workcenters/', views.workcenter_list, name='workcenter_list'),
    path('workcenters/<int:pk>/', views.workcenter_detail, name='workcenter_detail'),
    path('workcenters/new/', views.workcenter_create, name='workcenter_create'),
    path('workcenters/<int:pk>/edit/', views.workcenter_update, name='workcenter_update'),
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('classrooms/new/', views.classroom_create, name='classroom_create'),
    path('classrooms/<int:pk>/edit/', views.classroom_update, name='classroom_update'),
    path('schoolcycles/', views.schoolcycle_list, name='schoolcycle_list'),
    path('schoolcycles/new/', views.schoolcycle_create, name='schoolcycle_create'),
    path('schoolcycles/<int:pk>/edit/', views.schoolcycle_update, name='schoolcycle_update'),
    path('schoolperiods/new/', views.schoolperiod_create, name='schoolperiod_create'),
    path('schoolperiods/<int:pk>/edit/', views.schoolperiod_update, name='schoolperiod_update'),
    # Configuración de ciclos
    path('cycle-config/', views.cycle_config_list, name='cycle_config_list'),
    path('cycle-config/<int:work_center_id>/', views.cycle_config_update, name='cycle_config_update'),
    path('cycle-config/<int:work_center_id>/activation/', views.cycle_activation_management, name='cycle_activation_management'),
]
