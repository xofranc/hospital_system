from django.contrib.auth.models import User
from django.db import models
from common.models import Persona

class Paciente(Persona):
    numero_seguro_social = models.CharField(max_length=20, unique=True)
    historial_medico = models.TextField(blank=True)
    seguro_medico = models.CharField(max_length=100)


class Appointment:
    pass