# historias/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('crear_historia/', views.crear_historia_clinica, name='crear_historia_clinica'),
    path('historias/', views.listar_historias_clinicas, name='listar_historias_clinicas'),
    path('historias/<int:id>/', views.detalle_historia_clinica, name='detalle_historia_clinica'),
    path('historias/<int:id>/editar/', views.editar_historia_clinica, name='editar_historia_clinica'),
    path('historias/<int:id>/eliminar/', views.eliminar_historia_clinica, name='eliminar_historia_clinica'),
]


