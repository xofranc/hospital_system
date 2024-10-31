from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmacia, Producto
from .forms import FarmaciaForm, ProductoForm

# Vista para listar todas las farmacias
def lista_farmacias(request):
    farmacias = Farmacia.objects.all()  # Obtiene todas las farmacias
    return render(request, 'farmacias/lista_farmacias.html', {'farmacias': farmacias})

# Vista para mostrar el detalle de una farmacia específica
def detalle_farmacia(request, farmacia_id):
    farmacia = get_object_or_404(Farmacia, id=farmacia_id)  # Obtiene la farmacia o da error 404
    productos = Producto.objects.filter(farmacia=farmacia)  # Obtiene los productos de esa farmacia
    return render(request, 'farmacias/detalle_farmacia.html', {'farmacia': farmacia, 'productos': productos})

# Vista para agregar una nueva farmacia
def agregar_farmacia(request):
    if request.method == 'POST':  # Si se recibe un formulario
        form = FarmaciaForm(request.POST)
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda la nueva farmacia
            return redirect('lista_farmacias')  # Redirige a la lista de farmacias
    else:
        form = FarmaciaForm()  # Si es una solicitud GET, muestra un formulario vacío
    return render(request, 'farmacias/agregar_farmacia.html', {'form': form})

# Vista para agregar un nuevo producto
def agregar_producto(request):
    if request.method == 'POST':  # Si se recibe un formulario
        form = ProductoForm(request.POST)
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el nuevo producto
            return redirect('lista_farmacias')  # Redirige a la lista de farmacias
    else:
        form = ProductoForm()  # Si es una solicitud GET, muestra un formulario vacío
    return render(request, 'farmacias/agregar_producto.html', {'form': form})
