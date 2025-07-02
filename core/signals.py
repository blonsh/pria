from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Señal que crea un perfil de usuario cuando se crea un nuevo usuario.
    
    Args:
        sender: Modelo que envía la señal (User)
        instance: Instancia del usuario
        created: Booleano que indica si es una creación nueva
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Señal que guarda el perfil de usuario cuando se actualiza el usuario.
    
    Args:
        sender: Modelo que envía la señal (User)
        instance: Instancia del usuario
    """
    instance.userprofile.save()
