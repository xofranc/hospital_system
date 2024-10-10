from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PacienteLoginForm, PatientRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from recetarios.models import RecetaMedica
from .models import MedicalInfo, Appointment


# login
def paciente_login(request):
    if request.method == 'GET':
        return render(request, 'logins/login.html', {
            'form': AuthenticationForm()
        })
    else:
        # Autenticar al usuario
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Si la autenticación falla, mostrar un mensaje de error
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            # Si la autenticación es exitosa, loguear al usuario y redirigir
            login(request, user)
            return redirect('paciente_dashboard')

@login_required
def out(request):
    logout(request)
    return redirect('home')


# def paciente_register(request):
#     if request.method == "GET":
#         return render(request, 'logins/register.html', {
#             'form': AutheticationForm()
#         })
#     else:
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             try:
#                 user = form.save()  # Guarda al usuario con los datos validados
#                 login(request, user)  # Loguea al usuario
#                 return redirect('home')  # Redirige al usuario después del registro
#             except IntegrityError:
#                 return render(request, 'signup.html', {
#                     'form': form,
#                     'error': "El nombre de usuario ya existe"
#                 })
#         else:
#             return render(request, 'signup.html', {
#                 'form': form,
#                 'error': "Por favor corrige los errores a continuación"
#             })

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            # Guardar el usuario
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encriptar la contraseña
            user.save()
            messages.success(request, 'Tu cuenta ha sido creada. Puedes iniciar sesión ahora.')
            return redirect('paciente_login')  # Redirigir a la página de login después del registro
    else:
        form = PatientRegistrationForm()
    return render(request, 'logins/register.html', {'form': form})  # Renderizar la plantilla de registro


# login de los doctroes
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Solo permitir login a usuarios marcados como "staff" (doctores)
            login(request, user)
            return redirect('doctor_dashboard')  # Redirigir a una página de dashboard
        else:
            messages.error(request, 'Credenciales inválidas o no eres un doctor autorizado.')
    return render(request, 'logins/doctor_login.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'logins/doctor_dashboard.html')



@login_required
def paciente_dashboard(request):
    recetas = RecetaMedica.objects.filter(paciente=request.user)  # Obtener recetas del paciente actual
    return render(request, 'logins/paciente_dashboard.html', {'recetas': recetas})

@login_required
def medical_info_view(request):
    medical_info = MedicalInfo.objects.filter(patient=request.user).first()
    return render(request, 'logins/medical_info.html', {'medical_info': medical_info})

# Agendamiento de citas medicas
@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        date_time = request.POST.get('date_time')
        reason = request.POST.get('reason')
        Appointment.objects.create(patient=request.user, doctor=doctor, date_time=date_time, reason=reason)
        return redirect('dashboard')  # Redirige al dashboard después de agendar
    return render(request, 'logins/schedule_appointment.html')



# Home

def home(request):
    return render(request, 'logins/home.html')
