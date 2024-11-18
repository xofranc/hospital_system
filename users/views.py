from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import Doctor_register_form, Pacientes_register_form
from .models import Usuarios



# Create your views here.
def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
            # return HttpResponse('Loggeado')

        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'pacientes/login.html', {'form_paciente': form})


def paciente_register(request):
    if request.method == 'POST':
        form = Pacientes_register_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Usuarios.objects.create_user(role_data={
                'name': form.cleaned_data['name'],
                'last_name': form.cleaned_data['lastName'],
                'phone_number': form.cleaned_data['phone_number'],
                'address': form.cleaned_data['address'],
                'rh': form.cleaned_data['rh'],
                'estado_civil': form.cleaned_data['estado_civil'],
                'identification_number': form.cleaned_data['identification_number'],
            },base_data= {
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }, user_role='pacientes')
            messages.success(request, 'Registro exitoso.')
        else:
            print(form.errors)
    else:
        form = Pacientes_register_form()
    return render(request, 'pacientes/register.html', {'form_register_paciente': form})
        
        

def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'doctor/dashboard.html',)

        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'doctor/doctor_login.html', {'form_doctor': form})

def doctor_register(request):
    if request.method == 'POST':
        form = Doctor_register_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Usuarios.objects.create_user(role_data={
                'name': form.cleaned_data['name'],
                'last_name': form.cleaned_data['lastName'],
                'phone_number': form.cleaned_data['phone_number'],
                'address': form.cleaned_data['address'],
                'speciality': form.cleaned_data['speciality'],
                'licence_number': form.cleaned_data['licence_number'],
                'identification_number': form.cleaned_data['identification_number']
            }, base_data= {
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }, user_role='doctors')
            messages.success(request, 'Registro exitoso.')
        else:
            print(form.errors)
    else:
        form = Doctor_register_form()
    return render(request, 'doctor/register.html', {'form_register_doctor': form})

def home(request):
    return render(request, 'home.html')


def logout(request):
    pass