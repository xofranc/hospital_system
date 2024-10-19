from django.db import models
from common.models import Persona  # Asegúrate de que la ruta sea correcta

class Doctor(Persona):
    especialidad = models.CharField(max_length=100)
    pacientes_asignados = models.ManyToManyField('pacientes.Paciente', blank=True)

