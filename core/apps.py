from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Core'

    def ready(self):
        """
        Función que se ejecuta cuando la aplicación está lista.
        Se utiliza para registrar señales y otros inicializadores.
        """
        import core.signals  # Registrar señales si es necesario
