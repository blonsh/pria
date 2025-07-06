from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .models import PlanEstudio, SemestrePlan, MateriaPlan


@receiver(post_save, sender=PlanEstudio)
def actualizar_creditos_plan(sender, instance, created, **kwargs):
    """
    Actualiza automáticamente los créditos totales del plan de estudios
    cuando se crea o modifica un semestre.
    """
    if not created:  # Solo si no es una creación nueva
        # Recalcular créditos totales
        creditos_actuales = instance.get_creditos_actuales()
        if creditos_actuales != instance.creditos_totales:
            instance.creditos_totales = creditos_actuales
            # Evitar recursión infinita
            PlanEstudio.objects.filter(pk=instance.pk).update(
                creditos_totales=creditos_actuales
            )


@receiver(post_save, sender=SemestrePlan)
def actualizar_creditos_semestre(sender, instance, created, **kwargs):
    """
    Actualiza automáticamente los créditos del semestre cuando se agregan o modifican materias.
    """
    # Los créditos se actualizan automáticamente en el método save del modelo
    pass


@receiver(post_save, sender=MateriaPlan)
def actualizar_creditos_materia(sender, instance, created, **kwargs):
    """
    Actualiza automáticamente los créditos del semestre cuando se agrega o modifica una materia.
    """
    # Actualizar créditos del semestre
    semestre = instance.semestre
    semestre.creditos_semestre = semestre.get_creditos_semestre()
    SemestrePlan.objects.filter(pk=semestre.pk).update(
        creditos_semestre=semestre.creditos_semestre
    )
    
    # Actualizar créditos del plan
    plan = semestre.plan_estudio
    creditos_actuales = plan.get_creditos_actuales()
    if creditos_actuales != plan.creditos_totales:
        PlanEstudio.objects.filter(pk=plan.pk).update(
            creditos_totales=creditos_actuales
        )


@receiver(post_delete, sender=MateriaPlan)
def actualizar_creditos_eliminacion_materia(sender, instance, **kwargs):
    """
    Actualiza automáticamente los créditos cuando se elimina una materia.
    """
    # Actualizar créditos del semestre
    semestre = instance.semestre
    semestre.creditos_semestre = semestre.get_creditos_semestre()
    SemestrePlan.objects.filter(pk=semestre.pk).update(
        creditos_semestre=semestre.creditos_semestre
    )
    
    # Actualizar créditos del plan
    plan = semestre.plan_estudio
    creditos_actuales = plan.get_creditos_actuales()
    if creditos_actuales != plan.creditos_totales:
        PlanEstudio.objects.filter(pk=plan.pk).update(
            creditos_totales=creditos_actuales
        )


@receiver(post_delete, sender=SemestrePlan)
def actualizar_creditos_eliminacion_semestre(sender, instance, **kwargs):
    """
    Actualiza automáticamente los créditos del plan cuando se elimina un semestre.
    """
    plan = instance.plan_estudio
    creditos_actuales = plan.get_creditos_actuales()
    if creditos_actuales != plan.creditos_totales:
        PlanEstudio.objects.filter(pk=plan.pk).update(
            creditos_totales=creditos_actuales
        ) 