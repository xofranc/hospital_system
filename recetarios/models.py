from django.db import models
from django.contrib.auth.models import User

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del medicamento
    dosis = models.CharField(max_length=100)  # Dosis del medicamento (ej: "500mg")
    cantidad = models.PositiveIntegerField()  # Cantidad a prescribir
    descripcion = models.TextField(blank=True, null=True)  # Descripción o notas sobre el medicamento

    def __str__(self):
        return f"{self.nombre} - {self.dosis} ({self.cantidad})"


class Consulta(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultas')  # Paciente
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='consultas')  # Doctor
    fecha_consulta = models.DateTimeField(auto_now_add=True)  # Fecha de la consulta

    def __str__(self):
        return f"Consulta de {self.paciente.username} con el Dr. {self.doctor.username} en {self.fecha_consulta}"


class RecetaMedica(models.Model):
    ESTADOS = [
        ('activa', 'Activa'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')  # Paciente que recibe la receta
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recetas_doctor')  # Doctor que emite la receta
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='recetas', null=True)  # Relación a la consulta
    medicamentos = models.ManyToManyField(Medicamento)  # Relación muchos a muchos con medicamentos
    instrucciones = models.TextField()  # Instrucciones para el paciente
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    fecha_vencimiento = models.DateTimeField()  # Fecha de vencimiento de la receta
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')  # Estado de la receta
    notas_adicionales = models.TextField(blank=True, null=True)  # Notas adicionales del doctor

    def __str__(self):
        return f"Receta para {self.paciente.username} emitida por el Dr. {self.doctor.username} - Estado: {self.estado}"
