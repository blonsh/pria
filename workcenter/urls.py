from django.urls import path
from . import views

app_name = 'workcenter'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('workcenters/new/', views.workcenter_create, name='workcenter_create'),
    path('workcenters/<int:pk>/edit/', views.workcenter_update, name='workcenter_update'),
    path('classrooms/new/', views.classroom_create, name='classroom_create'),
    path('classrooms/<int:pk>/edit/', views.classroom_update, name='classroom_update'),
    path('schoolcycles/new/', views.schoolcycle_create, name='schoolcycle_create'),
    path('schoolcycles/<int:pk>/edit/', views.schoolcycle_update, name='schoolcycle_update'),
    path('schoolperiods/new/', views.schoolperiod_create, name='schoolperiod_create'),
    path('schoolperiods/<int:pk>/edit/', views.schoolperiod_update, name='schoolperiod_update'),
]
