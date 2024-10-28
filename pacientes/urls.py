from django.urls import path

from logins.views import register
from . import views
from .views import paciente_login

app_name = 'pacientes'

urlpatterns = [
    path('dashboard/', views.PacienteDashboardView.as_view(), name='dashboard'),
    path('login/', paciente_login, name='login'),
    path('logins/register/', views.register, name='register'),

]