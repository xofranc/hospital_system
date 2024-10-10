from django.db import models
from django.contrib.auth.models import User

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historias')  # Relación con el usuario (paciente)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='doctores')  # Relación con el doctor
    descripcion = models.TextField()  # Detalles de la historia clínica
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"Historia de {self.paciente.username} atendido por el Dr. {self.doctor.username}"
