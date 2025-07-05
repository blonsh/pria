from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Alumno
from core.models import Carrera


class AlumnoRegistrationForm(UserCreationForm):
    """
    Formulario para registrar un nuevo alumno con su perfil de usuario.
    """
    # Campos del usuario
    first_name = forms.CharField(
        label=_('Nombre'),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    last_name = forms.CharField(
        label=_('Apellidos'),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Ingresa tus apellidos'
        })
    )
    email = forms.EmailField(
        label=_('Correo electrónico'),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'ejemplo@correo.com'
        })
    )
    
    # Campos del alumno
    fecha_nacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'type': 'date'
        })
    )
    carrera = forms.ModelChoiceField(
        label=_('Carrera'),
        queryset=Carrera.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    numero_cuenta = forms.CharField(
        label=_('Número de cuenta'),
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Ingresa tu número de cuenta'
        })
    )
    foto = forms.ImageField(
        label=_('Foto de perfil'),
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'accept': 'image/*'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar widgets para los campos de contraseña
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Confirmar contraseña'
        })
        
        # Personalizar labels
        self.fields['username'].label = _('Nombre de usuario')
        self.fields['password1'].label = _('Contraseña')
        self.fields['password2'].label = _('Confirmar contraseña')
        
    def clean_numero_cuenta(self):
        """Validar que el número de cuenta sea único."""
        numero_cuenta = self.cleaned_data.get('numero_cuenta')
        if Alumno.objects.filter(numero_cuenta=numero_cuenta).exists():
            raise forms.ValidationError(_('Este número de cuenta ya está registrado.'))
        return numero_cuenta
        
    def clean_email(self):
        """Validar que el email sea único."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este correo electrónico ya está registrado.'))
        return email


class AlumnoUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar datos de un alumno existente.
    """
    first_name = forms.CharField(
        label=_('Nombre'),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    last_name = forms.CharField(
        label=_('Apellidos'),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    email = forms.EmailField(
        label=_('Correo electrónico'),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    
    class Meta:
        model = Alumno
        fields = ['fecha_nacimiento', 'carrera', 'numero_cuenta', 'foto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
                'type': 'date'
            }),
            'carrera': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'numero_cuenta': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
                'accept': 'image/*'
            })
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            
    def clean_numero_cuenta(self):
        """Validar que el número de cuenta sea único (excluyendo el actual)."""
        numero_cuenta = self.cleaned_data.get('numero_cuenta')
        if self.instance and self.instance.pk:
            if Alumno.objects.filter(numero_cuenta=numero_cuenta).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(_('Este número de cuenta ya está registrado.'))
        else:
            if Alumno.objects.filter(numero_cuenta=numero_cuenta).exists():
                raise forms.ValidationError(_('Este número de cuenta ya está registrado.'))
        return numero_cuenta 