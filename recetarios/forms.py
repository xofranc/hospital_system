from django import forms
from django.utils import timezone
from .models import RecetaMedica, Medicamento, Consulta
from django.contrib.auth.models import User

class RecetaMedicaForm(forms.ModelForm):
    ESTADOS = [
        ('activo', 'Activo'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    # Seleccionar el doctor que emite la receta
    
    doctor = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True),  # Suponiendo que los doctores son usuarios del tipo staff
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    # Selección de medicamentos de manera múltiple
    medicamentos = forms.ModelMultipleChoiceField(
        queryset=Medicamento.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Checkbox para seleccionar múltiples medicamentos
        required=True
    )
    
    # Campo para instrucciones
    instrucciones = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control'}),
        required=True
    )
    
    # Campo para fecha de vencimiento
    fecha_vencimiento = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        required=True
    )
    
    # Campo para notas adicionales
    notas_adicionales = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 15, 'class': 'form-control'}),
        required=False
    )

    # Campo para estado de la receta
    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    class Meta:
        model = RecetaMedica
        fields = ['paciente', 'doctor', 'medicamentos', 'instrucciones', 'fecha_vencimiento', 'notas_adicionales', 'estado']

    def clean_fecha_vencimiento(self):
        """
        Validación para asegurarse de que la fecha de vencimiento sea en el futuro.
        """
        fecha_vencimiento = self.cleaned_data.get('fecha_vencimiento')
        if fecha_vencimiento <= timezone.now():
            raise forms.ValidationError("La fecha de vencimiento debe ser en el futuro.")
        return fecha_vencimiento

    def clean(self):
        """
        Validación adicional para el formulario completo.
        """
        cleaned_data = super().clean()
        paciente = cleaned_data.get('paciente')
        estado = cleaned_data.get('estado')

        if estado == 'cancelada' and paciente:
            raise forms.ValidationError("No puedes cancelar la receta de un paciente sin un motivo.")

        return cleaned_data
