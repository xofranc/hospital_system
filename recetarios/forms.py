# recetarios/forms.py

from django import forms
from .models import RecetaMedica

class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = ['paciente', 'medicamentos', 'instrucciones']
