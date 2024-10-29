from django import forms
from .models import Usuarios, Doctors


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
        
            
        
    