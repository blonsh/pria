from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista básica para listar alumnos
@login_required
def alumno_list(request):
    """Vista para listar alumnos."""
    return render(request, 'alumnos/alumno_list.html')

# Vista básica para mostrar detalles de un alumno
@login_required
def alumno_detail(request, pk):
    """Vista para mostrar detalles de un alumno."""
    return render(request, 'alumnos/alumno_detail.html') 