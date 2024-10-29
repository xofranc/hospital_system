from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import Doctor_register_form
from .models import Usuarios



# Create your views here.
def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, '')

        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'doctor/login.html', {'forms': form})


def paciente_register(request):
    pass

def doctor_login(request):
    pass

def doctor_register(request):
    if request.method == 'POST':
        form = Doctor_register_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Usuarios.objects.create_user(role_data={
                'licence_number': form.cleaned_data['licence_number'],
                'name': form.cleaned_data['name'],
                'speciality': form.cleaned_data['speciality'],
                'last_name': form.cleaned_data['lastName'],
                'address': form.cleaned_data['address'],
                'phone_number': form.cleaned_data['phone_number'],
            }, base_data= {
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }, user_role='doctors')
            messages.success(request, 'Registro exitoso.')
        else:
            print(form.errors)
    else:
        form = Doctor_register_form()
    return render(request, 'doctor/register.html', {'form': form})