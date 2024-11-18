from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import HistoriaClinicaForm
from users.models import Pacientes, Doctors
from django.contrib.auth.decorators import login_required
from .models import Historia_clinica
from django.contrib.auth import login


# Create your views here.

@login_required
def crear_historia(request):
    if not hasattr(request.user, 'doctor'):
        messages.error(request, 'acceso no autorizado, Solo doctores pueden registrar historias clinicas')
        return render(request,'doctor/doctor_login.html', {'form_doctor': form})
    
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            historia_clinica.doctor = request.user.doctor
            historia_clinica.save()
            
            
            messages.success(request, 'Historia Clinica guardada con exito')
            return redirect('ver_historia_clinica', historia_clinica.id)  # Redirige a la vista de la historia clínica registrada
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        # Si la vista es GET, prellenamos el formulario si es necesario
        form = HistoriaClinicaForm()

    return render(request, 'historias_clinicas/registrar_historia_clinica.html', {'form': form})

@login_required
def ver_historia_clinica(request, historia_clinica_id):
    # Verificar que el usuario logueado sea un doctor
    if not hasattr(request.user, 'doctor'):
        messages.error(request, "Acceso no autorizado. Solo los doctores pueden ver las historias clínicas.")
        return redirect('login')

    # Obtiene la historia clínica para mostrarla después de guardarla
    historia_clinica = get_object_or_404(Historia_clinica, id=historia_clinica_id)

    return render(request, 'historias_clinicas/ver_historia_clinica.html', {'historia_clinica': historia_clinica})
        
        
        
        
@login_required
def ver_historia_clinica(request, historia_clinica_id):
    # Verificar que el usuario logueado sea un doctor
    if not hasattr(request.user, 'doctor'):
        messages.error(request, "Acceso no autorizado. Solo los doctores pueden ver las historias clínicas.")
        return redirect('login')

    # Obtiene la historia clínica para mostrarla después de guardarla
    historia_clinica = get_object_or_404(Historia_clinica, id=historia_clinica_id)

    return render(request, 'historias_clinicas/ver_historia_clinica.html', {'historia_clinica': historia_clinica}) 