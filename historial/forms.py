from django import forms
from .models import Historia_clinica, AlergiaMedicamento
from users.models import Pacientes


class HistoriaClinicaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Pacientes.objects.all(),
        empty_label='Seleccione el paciente',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    alergias = forms.ModelMultipleChoiceField(
        queryset=AlergiaMedicamento.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Historia_clinica
        fields = ['paciente', 'diagnostico', 'tratamiento', 'observaciones', 'alergias']
