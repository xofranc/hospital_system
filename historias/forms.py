# historias/forms.py

from django import forms
from .models import HistoriaClinica

#formulario 
class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica 
        fields = ['paciente', 'doctor', 'motivo_consulta', 'sintomas', 'diagnostico', 'tratamiento', 
            'observaciones', 'antecedentes_personales', 'antecedentes_familiares', 'alergias',
            'medicamentos_habituales', 'presion_arterial', 'frecuencia_cardiaca', 'temperatura', 
            'frecuencia_respiratoria', 'proximas_consultas', 'recomendaciones']  # Campos que queremos que se incluyan en el formulario
        widgets={
            'sintomas': forms.Textarea(attrs={'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
            'observaciones': forms.Textarea(attrs={'rows': 2}),
            'antecedentes_personales': forms.Textarea(attrs={'rows': 3}),
            'antecedentes_familiares': forms.Textarea(attrs={'rows': 3}),
            'alergias': forms.Textarea(attrs={'rows': 2}),
            'medicamentos_habituales': forms.Textarea(attrs={'rows': 2}),
            'recomendaciones': forms.Textarea(attrs={'rows': 2}),
        }