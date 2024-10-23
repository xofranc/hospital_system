from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HistoriaClinicaForm
from .models import HistoriaClinica


@login_required
def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia = form.save(commit=False)
            historia.doctor = request.user  # Asignamos el doctor actual
            historia.save()
            return redirect('doctor_dashboard')  # Redirigir al dashboard después de guardar
    else:
        form = HistoriaClinicaForm()

    return render(request, 'historias/crear_historia_clinica.html', {'form': form})


@login_required
def doctor_dashboard(request):
    historias = HistoriaClinica.objects.filter(doctor=request.user)  # Obtener las historias clínicas del doctor actual
    return render(request, 'logins/../templates/doctores/doctor_dashboard.html', {'historias': historias})