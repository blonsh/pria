from django import forms
from .models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod

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
        fields = ['work_center', 'name', 'start_date', 'end_date']

class SchoolPeriodForm(forms.ModelForm):
    class Meta:
        model = SchoolPeriod
        fields = ['school_cycle', 'name', 'period_type', 'start_date', 'end_date']
