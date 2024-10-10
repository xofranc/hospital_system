from django.urls import path
from . import views
from .views import medical_info_view, schedule_appointment



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.paciente_login, name='paciente_login'),
    path('register/', views.register, name='register'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('medical-info/', medical_info_view, name='medical_info'),
    path('schedule-appointment/', schedule_appointment, name='schedule_appointment'),  # Nueva URL
    path('logout/', views.out, name='logout'),

]
