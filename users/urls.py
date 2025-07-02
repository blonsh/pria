from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('roles/new/', views.role_create, name='role_create'),
    path('roles/<int:pk>/edit/', views.role_update, name='role_update'),
    path('users/new/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
]
