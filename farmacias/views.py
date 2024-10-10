# farmacias/views.py

from django.shortcuts import render, redirect
from .forms import EnviarRecetaForm


def enviar_receta(request):
    if request.method == 'POST':
        form = EnviarRecetaForm(request.POST)
        if form.is_valid():
            # Aquí enviarías la receta a la farmacia usando, por ejemplo, un API
            # Simularemos el envío simplemente mostrando un mensaje
            farmacia = form.cleaned_data['farmacia']
            receta_id = form.cleaned_data['receta_id']
            # Enviar a la farmacia (aquí podrías agregar lógica para hacer una llamada API)
            return redirect('listar_recetas_medicas')  # Redirigir después de enviar
    else:
        form = EnviarRecetaForm()

    return render(request, 'farmacias/enviar_receta.html', {'form': form})
