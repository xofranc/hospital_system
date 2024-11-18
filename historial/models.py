from django.db import models
from users.models import Pacientes, Doctors
# from multiselectfield import MultiSelectField
# Create your models here.


class Historia_clinica(models.Model):
        paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='historias')
        doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True, related_name='historias_atendidas')
        fecha_creacion = models.DateTimeField(auto_now_add=True)
        diagnostico = models.TextField()
        tratamiento = models.TextField()
        alergias = models.ManyToManyField('AlergiaMedicamento', blank=True)
        antecedentes_medicos = models.TextField(blank=True)
        historial_enfermedades = models.TextField(blank=True)
        observaciones = models.TextField(blank=True)



class AlergiaMedicamento(models.Model):
    nombre = models.CharField(max_length=100)
    

