import os
from django.core.wsgi import get_wsgi_application

# Determinar la configuración según el entorno
if os.getenv('DJANGO_ENV') == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

application = get_wsgi_application()
