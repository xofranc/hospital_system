# recetarios/views.py
from django.urls import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.template.loader import render_to_string


from .forms import RecetaMedicaForm
from .models import RecetaMedica


@login_required
def crear_receta_medica(request):
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.doctor = request.user  # Asignamos el doctor actual
            receta.save()
            return redirect('doctor_dashboard')  # Redirigir al dashboard después de guardar
    else:
        form = RecetaMedicaForm()

    return render(request, 'recetarios/crear_receta_medica.html', {'form': form})


@login_required
def listar_recetas_medicas(request):
    recetas = RecetaMedica.objects.filter(doctor=request.user)  # Obtener las recetas del doctor actual
    return render(request, 'recetarios/listar_recetas_medicas.html', {'recetas': recetas})


@login_required
def generar_pdf_receta(request, receta_id):
    receta = RecetaMedica.objects.get(id=receta_id)

    # Renderizar la plantilla HTML para el PDF
    html_string = render_to_string('recetarios/pdf_receta_medica.html', {'receta': receta})
    html = HTML(string=html_string)

    # Crear un HTTPResponse con el contenido del PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receta_{receta_id}.pdf"'

    # Escribir el PDF en la respuesta
    html.write_pdf(response)
    return response

def otra_vista(request):
    url_listar_recetarios = reverse('recetarios:listar_recetarios')
    return render(request, 'otra_plantilla.html',{'url': url_listar_recetarios})