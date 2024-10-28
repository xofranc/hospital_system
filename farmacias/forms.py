from django import forms # type: ignore
from .models import Proveedor, Medicamento, Cliente, Venta

# Formulario basado en el modelo Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        # Especificamos el modelo y los campos a incluir en el formulario
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']
        widgets = {
            # Configuramos el widget del campo 'direccion' para usar un Textarea
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario basado en el modelo Medicamento
class MedicamentoForm(forms.ModelForm):
    class Meta:
        # Especificamos el modelo y los campos a incluir en el formulario
        model = Medicamento
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible', 'proveedor']
        widgets = {
            # Configuramos el widget del campo 'descripcion' para usar un Textarea
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario basado en el modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        # Especificamos el modelo y los campos a incluir en el formulario
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']
        widgets = {
            # Configuramos el widget del campo 'direccion' para usar un Textarea
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario basado en el modelo Venta
class VentaForm(forms.ModelForm):
    class Meta:
        # Especificamos el modelo y los campos a incluir en el formulario
        model = Venta
        fields = ['cliente', 'medicamento', 'cantidad']
