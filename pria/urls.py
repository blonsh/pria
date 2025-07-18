from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('workcenter/', include('workcenter.urls')),
    path('planes-estudio/', include('planes_estudio.urls')),
    path('alumnos/', include('alumnos.urls')),
    path('asistencia/', include('asistencia.urls')),
]
