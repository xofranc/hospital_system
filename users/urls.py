from django.urls import path

from . import views


urlpatterns = [
    path('paciente/login/', views.paciente_login, name='paciente_login'),
    path('doctor/register', views.doctor_register, name= 'doctor_register'),
]
