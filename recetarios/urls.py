# recetarios/urls.py

from django.urls import path
from . import views

app_name = 'recetarios'

urlpatterns = [
    path('crear/', views.crear_receta_medica, name='crear_receta_medica'),  # Ruta para crear recetas
    path('listar/', views.listar_recetas_medicas, name='listar_recetas_medicas'),  # Ruta para listar recetas
    path('pdf/<int:receta_id>/', views.generar_pdf_receta, name='generar_pdf_receta'),  # Nueva URL para PDF

]
