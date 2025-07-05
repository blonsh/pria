from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista básica para listar docentes
@login_required
def docente_list(request):
    """Vista para listar docentes."""
    return render(request, 'docentes/docente_list.html')

# Vista básica para mostrar detalles de un docente
@login_required
def docente_detail(request, pk):
    """Vista para mostrar detalles de un docente."""
    return render(request, 'docentes/docente_detail.html') 