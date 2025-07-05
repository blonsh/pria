from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register_user'),
    path('register/alumno/', views.register_alumno, name='register_alumno'),
    path('register/docente/', views.register_docente, name='register_docente'),
    # URLs de Django para reset de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # URLs de apps
    path('asistencia/', include('asistencia.urls', namespace='asistencia')),
    path('alumnos/', include('alumnos.urls', namespace='alumnos')),
    path('docentes/', include('docentes.urls', namespace='docentes')),
]
