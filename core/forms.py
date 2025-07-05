from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import UserProfile
from alumnos.models import Alumno
from docentes.models import Docente

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
        fields = ('fecha_nacimiento', 'carrera', 'numero_cuenta')
        
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
