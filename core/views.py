from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """
    Vista principal de la aplicación.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza la página principal
    """
    return render(request, 'core/home.html')
