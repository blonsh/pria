from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Asistencia
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Asistencia)
def enviar_notificacion_asistencia(sender, instance, created, **kwargs):
    """
    Señal que se ejecuta cuando se crea una nueva asistencia.
    Envía una notificación al docente y al alumno.
    """
    if created:
        # Notificar al docente
        if instance.docente and instance.docente.user.email:
            subject = f'Nueva asistencia registrada - {instance.alumno.user.get_full_name()}'
            message = f'Se ha registrado la asistencia del alumno {instance.alumno.user.get_full_name()}\n\n'
            message += f'Fecha: {instance.fecha}\n'
            message += f'Estado: {instance.get_estado_display()}\n'
            message += f'Hora de entrada: {instance.hora_entrada}\n'
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.docente.user.email]
            )
            
        # Notificar al alumno
        if instance.alumno.user.email:
            subject = f'Tu asistencia ha sido registrada - {instance.fecha}'
            message = f'Tu asistencia ha sido registrada para la fecha {instance.fecha}\n\n'
            message += f'Estado: {instance.get_estado_display()}\n'
            message += f'Hora de entrada: {instance.hora_entrada}\n'
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.alumno.user.email]
            )
