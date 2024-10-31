from django.urls import path
from . import views

# Define las rutas para las vistas de la aplicación 'farmacias'
urlpatterns = [
    path('', views.lista_farmacias, name='lista_farmacias'),  # Página principal que muestra todas las farmacias
    path('<int:farmacia_id>/', views.detalle_farmacia, name='detalle_farmacia'),  # Detalle de una farmacia específica
    path('agregar/', views.agregar_farmacia, name='agregar_farmacia'),  # Formulario para agregar una nueva farmacia
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),  # Formulario para agregar un nuevo producto
]
