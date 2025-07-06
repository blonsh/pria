from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import (
    PlanEstudio, SemestrePlan, MateriaPlan, Competencia,
    ObjetivoEducativo, PerfilEgreso, VersionPlanEstudio
)


class PlanEstudioForm(forms.ModelForm):
    """
    Formulario para crear y editar planes de estudios.
    """
    class Meta:
        model = PlanEstudio
        fields = [
            'nombre', 'descripcion', 'carrera', 'work_center',
            'ciclo_inicio', 'duracion_semestres', 'creditos_totales',
            'estado'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'placeholder': _('Nombre del plan de estudios')
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Descripción del plan de estudios')
            }),
            'duracion_semestres': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1,
                'max': 20
            }),
            'creditos_totales': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
            'carrera': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
            'work_center': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
            'ciclo_inicio': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        carrera = cleaned_data.get('carrera')
        work_center = cleaned_data.get('work_center')
        nombre = cleaned_data.get('nombre')
        
        if carrera and work_center and nombre:
            # Verificar que no exista un plan con el mismo nombre para la misma carrera y centro
            if PlanEstudio.objects.filter(
                carrera=carrera,
                work_center=work_center,
                nombre=nombre
            ).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise ValidationError(
                    _('Ya existe un plan de estudios con este nombre para la carrera y centro de trabajo seleccionados.')
                )
        
        return cleaned_data


class SemestrePlanForm(forms.ModelForm):
    """
    Formulario para crear y editar semestres de un plan de estudios.
    """
    class Meta:
        model = SemestrePlan
        fields = ['numero_semestre', 'nombre', 'es_optativo', 'descripcion']
        widgets = {
            'numero_semestre': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'placeholder': _('Nombre del semestre (opcional)')
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 3,
                'placeholder': _('Descripción del semestre')
            }),
            'es_optativo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        plan_estudio = cleaned_data.get('plan_estudio')
        numero_semestre = cleaned_data.get('numero_semestre')
        
        if plan_estudio and numero_semestre:
            # Verificar que no exista un semestre con el mismo número en el mismo plan
            if SemestrePlan.objects.filter(
                plan_estudio=plan_estudio,
                numero_semestre=numero_semestre
            ).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise ValidationError(
                    _('Ya existe un semestre con este número en el plan de estudios.')
                )
            
            # Verificar que el número de semestre no exceda la duración del plan
            if numero_semestre > plan_estudio.duracion_semestres:
                raise ValidationError(
                    _('El número de semestre no puede exceder la duración del plan de estudios.')
                )
        
        return cleaned_data


class MateriaPlanForm(forms.ModelForm):
    """
    Formulario para crear y editar materias de un plan de estudios.
    """
    class Meta:
        model = MateriaPlan
        fields = [
            'materia', 'tipo_materia', 'creditos', 'horas_teoria',
            'horas_practica', 'horas_independiente', 'orden'
        ]
        widgets = {
            'materia': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
            'tipo_materia': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
            'creditos': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
            'horas_teoria': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 0
            }),
            'horas_practica': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 0
            }),
            'horas_independiente': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 0
            }),
            'orden': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        semestre = cleaned_data.get('semestre')
        materia = cleaned_data.get('materia')
        orden = cleaned_data.get('orden')
        
        if semestre and materia:
            # Verificar que no exista la misma materia en el mismo semestre
            if MateriaPlan.objects.filter(
                semestre=semestre,
                materia=materia
            ).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise ValidationError(
                    _('Esta materia ya está asignada al semestre.')
                )
        
        if semestre and orden:
            # Verificar que no exista el mismo orden en el semestre
            if MateriaPlan.objects.filter(
                semestre=semestre,
                orden=orden
            ).exclude(pk=self.instance.pk if self.instance else None).exists():
                raise ValidationError(
                    _('Ya existe una materia con este orden en el semestre.')
                )
        
        return cleaned_data


class CompetenciaForm(forms.ModelForm):
    """
    Formulario para crear y editar competencias.
    """
    class Meta:
        model = Competencia
        fields = ['nombre', 'descripcion', 'tipo_competencia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'placeholder': _('Nombre de la competencia')
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Descripción de la competencia')
            }),
            'tipo_competencia': forms.Select(attrs={
                'class': 'form-select rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500'
            }),
        }


class ObjetivoEducativoForm(forms.ModelForm):
    """
    Formulario para crear y editar objetivos educativos.
    """
    class Meta:
        model = ObjetivoEducativo
        fields = ['titulo', 'descripcion', 'orden']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'placeholder': _('Título del objetivo')
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Descripción del objetivo')
            }),
            'orden': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
        }


class PerfilEgresoForm(forms.ModelForm):
    """
    Formulario para crear y editar perfiles de egreso.
    """
    class Meta:
        model = PerfilEgreso
        fields = [
            'descripcion_general', 'competencias_generales',
            'competencias_especificas', 'campo_laboral'
        ]
        widgets = {
            'descripcion_general': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Descripción general del perfil de egreso')
            }),
            'competencias_generales': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Competencias generales que desarrolla el egresado')
            }),
            'competencias_especificas': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Competencias específicas que desarrolla el egresado')
            }),
            'campo_laboral': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Campo laboral donde puede desempeñarse el egresado')
            }),
        }


class VersionPlanEstudioForm(forms.ModelForm):
    """
    Formulario para crear versiones de planes de estudios.
    """
    class Meta:
        model = VersionPlanEstudio
        fields = ['numero_version', 'cambios_descripcion', 'es_activa']
        widgets = {
            'numero_version': forms.NumberInput(attrs={
                'class': 'form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'min': 1
            }),
            'cambios_descripcion': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border-gray-300 focus:border-blue-500 focus:ring-blue-500',
                'rows': 4,
                'placeholder': _('Descripción de los cambios en esta versión')
            }),
            'es_activa': forms.CheckboxInput(attrs={
                'class': 'form-checkbox rounded border-gray-300 text-blue-600 focus:ring-blue-500'
            }),
        } 