# recetarios/models.py

from django.db import models
from django.contrib.auth.models import User

class RecetaMedica(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')  # Paciente que recibirá la receta
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recetas_doctor')  # Doctor que emite la receta
    medicamentos = models.TextField()  # Lista de medicamentos prescritos
    instrucciones = models.TextField()  # Instrucciones para el paciente
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"Receta para {self.paciente.username} emitida por el Dr. {self.doctor.username}"
