from django import forms
from .models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod, SchoolCycleConfig

class WorkCenterForm(forms.ModelForm):
    class Meta:
        model = WorkCenter
        fields = ['name', 'address', 'director_name', 'school_control_name']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['work_center', 'name', 'capacity']

class SchoolCycleForm(forms.ModelForm):
    class Meta:
        model = SchoolCycle
        fields = ['work_center', 'name', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SchoolCycleConfigForm(forms.ModelForm):
    class Meta:
        model = SchoolCycleConfig
        fields = ['allow_multiple_active', 'auto_activate_by_date']
        widgets = {
            'allow_multiple_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto_activate_by_date': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class SchoolPeriodForm(forms.ModelForm):
    class Meta:
        model = SchoolPeriod
        fields = ['school_cycle', 'name', 'period_type', 'start_date', 'end_date']
