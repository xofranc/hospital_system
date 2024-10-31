from django import forms
from .models import Usuarios, Doctors, Paciente


class Doctor_register_form(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    phone_number = forms.CharField(max_length=10)
    name = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    licence_number = forms.IntegerField()
    speciality = forms.CharField(max_length=50)
    identification_number = forms.IntegerField()
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuarios.objects.filter(email=email).first():
            raise forms.ValidationError("El correo electrónico ya está registrado")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('password')
        if Doctors.objects.filter(phone_number=phone_number).first():
            raise forms.ValidationError("El número de teléfono ya está registrado")
        return phone_number
        
    def clean_licence_number(self):
        licence_number = self.cleaned_data.get('licence_number')
        if Doctors.objects.filter(licence_number=licence_number).first():
            raise forms.ValidationError("El número de licencia ya está registrado")
        return licence_number
    
    def clean_identifcation_number(self):
        identification_number = self.cleaned_data.get('identification_number')
        if Paciente.objects.filter(identification_number=identification_number).first():
            raise forms.ValidationError("El número de identificación ya está registrado")
        
            
        
class Paciente_register_form(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    phone_number = forms.CharField(max_length=10)
    name = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    rh = forms.CharField(max_length=5)
    address = forms.CharField(max_length=100)
    estado_civil = forms.CharField(max_length=30)
    identification_number = forms.IntegerField()
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuarios.objects.filter(email=email).first():
            raise forms.ValidationError("El correo electrónico ya está registrado")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Paciente.objects.filter(phone_number=phone_number).first():
            raise forms.ValidationError("El número de teléfono ya está registrado")
        return phone_number
    
    def clean_identification_number(self):
        identification_number = self.cleaned_data.get('identification_number')
        if Paciente.objects.filter(identification_number=identification_number).first():
            raise forms.ValidationError("El número de identificación ya está registrado")
        return identification_number
    
class Paciente_login_form(forms.Form):
    
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)