# historias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_historia_clinica, name='crear_historia_clinica'),  # Ruta para crear historias clínicas
]
