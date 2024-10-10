from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Paciente
from django.contrib.auth.models import User


class PacienteLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo Electrónico", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Paciente
        fields = ['username', 'password']

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  # Usamos el modelo User para manejar la autenticación
        fields = ['username', 'email', 'password']  # Campos del formulario

    password = forms.CharField(widget=forms.PasswordInput)  # Para ocultar la contraseña al escribir