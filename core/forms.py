from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import UserProfile
from alumnos.models import Alumno
from docentes.models import Docente
from .models import Matricula, Curso
from django.db import models

class UserRegistrationForm(UserCreationForm):
    """
    Formulario para el registro de usuarios.
    """
    email = forms.EmailField(required=True, label=_('Correo electrónico'))
    first_name = forms.CharField(required=True, label=_('Nombre'))
    last_name = forms.CharField(required=True, label=_('Apellido'))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label,
            })

class AlumnoRegistrationForm(forms.ModelForm):
    """
    Formulario para el registro de alumnos.
    """
    class Meta:
        model = Alumno
        fields = ('fecha_nacimiento', 'work_center', 'programa_academico')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class DocenteRegistrationForm(forms.ModelForm):
    """
    Formulario para el registro de docentes.
    """
    class Meta:
        model = Docente
        fields = ('especialidad', 'fecha_contratacion')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class MatriculaForm(forms.ModelForm):
    """
    Formulario para matricular un alumno en un curso.
    """
    class Meta:
        model = Matricula
        fields = ['alumno', 'curso']
        widgets = {
            'alumno': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'curso': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo cursos activos y con cupo disponible
        self.fields['curso'].queryset = Curso.objects.filter(
            cupo_maximo__gt=Matricula.objects.values('curso').annotate(
                count=models.Count('id')
            ).filter(curso=models.OuterRef('pk')).values('count')[:1]
        )
    
    def clean(self):
        cleaned_data = super().clean()
        alumno = cleaned_data.get('alumno')
        curso = cleaned_data.get('curso')
        
        if alumno and curso:
            # Verificar si ya está matriculado
            if Matricula.objects.filter(alumno=alumno, curso=curso).exists():
                raise forms.ValidationError(_('Este alumno ya está matriculado en este curso.'))
            
            # Verificar cupo disponible
            matriculados = Matricula.objects.filter(curso=curso).count()
            if matriculados >= curso.cupo_maximo:
                raise forms.ValidationError(_('Este curso ya no tiene cupo disponible.'))
        
        return cleaned_data

class BuscarMatriculaForm(forms.Form):
    """
    Formulario para buscar matrículas.
    """
    alumno = forms.ModelChoiceField(
        queryset=Alumno.objects.all(),
        required=False,
        label=_('Alumno'),
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        required=False,
        label=_('Curso'),
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    fecha_inicio = forms.DateField(
        required=False,
        label=_('Fecha de inicio'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    fecha_fin = forms.DateField(
        required=False,
        label=_('Fecha de fin'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
