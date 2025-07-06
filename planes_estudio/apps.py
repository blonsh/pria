from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlanesEstudioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'planes_estudio'
    verbose_name = _('Planes de Estudios')
    
    def ready(self):
        import planes_estudio.signals
