from django.urls import path

from . import views


urlpatterns = [
    path('paciente/dashboard/', views.dashboard_paciente, name='dashboard'),
    path('doctor/dashboard/', views.dashboard_doctor, name='dashboard_doctor'),

]