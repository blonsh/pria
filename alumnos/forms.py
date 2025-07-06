from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import re
from .models import Alumno
from core.models import AcademicProgram, Genero
from workcenter.models import WorkCenter





class AlumnoRegistrationForm(UserCreationForm):
    """
    Formulario para registrar un nuevo alumno con su perfil de usuario.
    """
    # CURP primero (identificador único)
    curp = forms.CharField(
        label=_('CURP'),
        max_length=18,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'ABCD123456EFGHIJ78',
            'pattern': '[A-Z0-9]{18}',
            'title': 'CURP debe tener exactamente 18 caracteres alfanuméricos'
        }),
        help_text=_('Clave Única de Registro de Población (18 caracteres)')
    )
    
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
            'placeholder': 'correo@ejemplo.com'
        })
    )
    
    # Campos del alumno
    fecha_nacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'id': 'fecha_nacimiento_field'
        }),
        help_text=_('Ingresa tu fecha de nacimiento')
    )
    work_center = forms.ModelChoiceField(
        label=_('Centro de Trabajo'),
        queryset=WorkCenter.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    programa_academico = forms.ModelChoiceField(
        label=_('Programa Académico'),
        queryset=AcademicProgram.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    
    # Campo de género
    genero = forms.ModelChoiceField(
        label=_('Género'),
        queryset=None,  # Se establecerá en __init__
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
        })
    )
    
    # Campos de contacto
    telefono_contacto = forms.CharField(
        label=_('Teléfono de contacto'),
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': '555-123-4567'
        })
    )
    nombre_contacto_emergencia = forms.CharField(
        label=_('Nombre del contacto de emergencia'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': 'Nombre completo del contacto'
        })
    )
    telefono_contacto_emergencia = forms.CharField(
        label=_('Teléfono del contacto de emergencia'),
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent',
            'placeholder': '555-123-4567'
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
        
        # Importar Genero aquí para evitar problemas de importación circular
        from core.models import Genero
        
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
        
        # Configurar queryset para género
        self.fields['genero'].queryset = Genero.objects.filter(activo=True)
        
    def clean_curp(self):
        """Validar formato y unicidad del CURP."""
        curp = self.cleaned_data.get('curp')
        
        if not curp:
            raise forms.ValidationError(_('El CURP es obligatorio.'))
        
        # Validar longitud
        if len(curp) != 18:
            raise forms.ValidationError(_('El CURP debe tener exactamente 18 caracteres.'))
        
        # Validar que solo contenga letras y números
        if not re.match(r'^[A-Z0-9]{18}$', curp):
            raise forms.ValidationError(_('El CURP solo puede contener letras mayúsculas y números.'))
        
        # Validar unicidad
        if Alumno.objects.filter(curp=curp).exists():
            # Obtener información del alumno existente
            alumno_existente = Alumno.objects.get(curp=curp)
            raise forms.ValidationError(
                _('Este CURP ya está registrado para el alumno: %(nombre)s - Matrícula: %(matricula)s - Número de cuenta: %(cuenta)s') % {
                    'nombre': alumno_existente.user.get_full_name(),
                    'matricula': alumno_existente.numero_cuenta,
                    'cuenta': alumno_existente.numero_cuenta
                }
            )
        
        return curp.upper()
        
    def clean_telefono_contacto(self):
        """Validar formato del teléfono de contacto."""
        telefono = self.cleaned_data.get('telefono_contacto')
        if telefono:
            # Limpiar el teléfono de caracteres especiales
            telefono_limpio = re.sub(r'[^\d]', '', telefono)
            if len(telefono_limpio) < 10:
                raise forms.ValidationError(_('El teléfono debe tener al menos 10 dígitos.'))
        return telefono
        
    def clean_telefono_contacto_emergencia(self):
        """Validar formato del teléfono de emergencia."""
        telefono = self.cleaned_data.get('telefono_contacto_emergencia')
        if telefono:
            # Limpiar el teléfono de caracteres especiales
            telefono_limpio = re.sub(r'[^\d]', '', telefono)
            if len(telefono_limpio) < 10:
                raise forms.ValidationError(_('El teléfono debe tener al menos 10 dígitos.'))
        return telefono
        
    def clean_email(self):
        """Validar que el email sea único."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este correo electrónico ya está registrado.'))
        return email

    def clean(self):
        """Validar que las contraseñas coincidan."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_('Las contraseñas no coinciden. Por favor, asegúrate de que ambas contraseñas sean idénticas.'))
        
        return cleaned_data


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
        fields = ['fecha_nacimiento', 'work_center', 'programa_academico', 'genero', 'foto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'work_center': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'programa_academico': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent'
            }),
            'genero': forms.Select(attrs={
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
            
    def clean_email(self):
        """Validar que el email sea único."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este correo electrónico ya está registrado.'))
        return email

    def clean_fecha_nacimiento(self):
        """Validar que la fecha de nacimiento sea válida."""
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > datetime.date.today():
            raise forms.ValidationError(_('La fecha de nacimiento no puede ser en el futuro.'))
        return fecha_nacimiento

    def clean_work_center(self):
        """Validar que el centro de trabajo sea válido."""
        work_center = self.cleaned_data.get('work_center')
        if not work_center:
            raise forms.ValidationError(_('Debe seleccionar un centro de trabajo.'))
        return work_center

    def clean_programa_academico(self):
        """Validar que el programa académico sea válido."""
        programa_academico = self.cleaned_data.get('programa_academico')
        if not programa_academico:
            raise forms.ValidationError(_('Debe seleccionar un programa académico.'))
        return programa_academico

    def clean_foto(self):
        """Validar que la foto de perfil sea válida."""
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError(_('Debe seleccionar una foto de perfil.'))
        return foto 