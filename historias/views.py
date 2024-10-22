from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HistoriaClinicaForm
from .models import HistoriaClinica


# Vista para crear una nueva historia clínica
def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():  # Verificamos si el formulario es válido
            form.save()  # Guardamos la historia clínica en la base de datos
            return redirect('nombre_de_la_vista_o_url_a_redirigir')  # Redirigimos tras guardar
    else:
        form = HistoriaClinicaForm()  # Creamos un formulario vacío si es GET

    return render(request, 'historias/historia_clinica_form.html', {'form': form})  # Renderizamos la plantilla con el formulario


#vista para listar todas las historias clinicas
def listar_historias_clinicas(request):
    #obtenemos todas las historias clinicas en la base de datos
    historias=HistoriaClinica.objects.all()
    return render(request, 'historias/lista_historias_clinicas-html', {'historias': historias})


# Vista para mostrar el detalle de una historia clínica
def detalle_historia_clinica(request, id):
    # Obtenemos la historia clínica por su ID
    historia = HistoriaClinica.objects.get(id=id)
    return render(request, 'historias/detalle_historia_clinica.html', {'historia': historia})

# Vista para editar una historia clínica
def editar_historia_clinica(request, id):
    historia = HistoriaClinica.objects.get(id=id)
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect('detalle_historia_clinica', id=historia.id)
    else:
        form = HistoriaClinicaForm(instance=historia)
    return render(request, 'historias/historia_clinica_form.html', {'form': form})

# Vista para eliminar una historia clínica
def eliminar_historia_clinica(request, id):
    historia = HistoriaClinica.objects.get(id=id)
    if request.method == 'POST':
        historia.delete()
        return redirect('listar_historias_clinicas')
    return render(request, 'historias/eliminar_historia_clinica.html', {'historia': historia})
