from django import forms

from .models import StudentVehicle

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentVehicle
        exclude = [' is_approved']
