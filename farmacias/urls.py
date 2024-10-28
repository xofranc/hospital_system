# farmacias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_receta, name='enviar_receta'),  # Nueva URL para enviar receta
]
