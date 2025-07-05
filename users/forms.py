from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from .models import User, Role

class RoleForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm',
            'placeholder': 'Describe las responsabilidades y funciones de este rol...'
        }),
        required=False,
        max_length=1000,  # Aumentar el límite para permitir descripciones más largas
        help_text='Describe las responsabilidades y funciones de este rol (máximo 1000 caracteres)'
    )
    
    class Meta:
        model = Role
        fields = ['name', 'description', 'permissions']

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description and len(description) > 1000:
            raise forms.ValidationError('La descripción no puede superar los 1000 caracteres.')
        return description

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        required=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
