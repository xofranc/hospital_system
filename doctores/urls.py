from django.urls import path

from . import views

app_name = 'doctores'
urlpatterns = [
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
