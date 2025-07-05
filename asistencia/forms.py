from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    """Formulario para registrar asistencia"""
    class Meta:
        model = Asistencia
        fields = ['alumno', 'fecha', 'estado', 'hora_entrada', 'hora_salida', 'docente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
        }

class BuscarAsistenciaForm(forms.Form):
    """Formulario para buscar asistencia"""
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    alumno = forms.ModelChoiceField(
        queryset=None,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alumno'].queryset = Asistencia.objects.all()
