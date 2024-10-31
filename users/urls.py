from django.urls import path

from . import views


urlpatterns = [
    path('paciente/login/', views.paciente_login, name='paciente_login'),
    path('paciente/register/', views.paciente_register, name='paciente_register'),
    path('doctor/register/', views.doctor_register, name= 'doctor_register'),
    path('doctor/login/', views.doctor_login, name= 'doctor_login'),
    path('', views.home, name='home'),
]
