from django.urls import path
from . import views
from .views import medical_info_view, schedule_appointment

app_name = 'logins'

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.paciente_login, name='paciente_login'),
    path('register/', views.register, name='register'),

    path('medical-info/', medical_info_view, name='medical_info'),
    path('schedule-appointment/', schedule_appointment, name='schedule_appointment'),  # Nueva URL
    # path('logout/', views.out, name='logout'),

]
