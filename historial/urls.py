from django.urls import path
from . import views

urlpatterns = [
    path('nueva_historia/', views.crear_historia, name='crear_historia'),
    path('ver_historia/', views.ver_historia_clinica, name='ver_historia')
]
