# historias/forms.py

from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'descripcion']  # Selecciona el paciente y añade la descripción de la historia
