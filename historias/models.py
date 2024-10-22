from django.db import models
from django.contrib.auth.models import User

#modelo para la historia clinica
class HistoriaClinica(models.Model):
    #relacion del paciente y el doctor
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historias_pacientes')  # Relación con el usuario (paciente)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='historias_doctor')  # Relación con el doctor

    #datos para la consulta
    fecha_consulta=models.DateTimeField(auto_now_add=True)#fecha automatica de cuando se crea la historia
    motivo_consulta=models.TextField()#motivo por el cual va a consulta
    sintomas=models.TextField()#sintomas que tenga el paciente
    diagnostico=models.TextField()#diagnostico formulado por el doctor
    tratamiento=models.TextField()#tratamiendo recomendado por el doctor
    observaciones=models.TextField(blank=True,null=True)#observaciones adicionales dadas por el doctor

    #informacion adicional
    antecedentes_personales = models.TextField()  # Antecedentes médicos personales
    antecedentes_familiares = models.TextField()  # Antecedentes médicos familiares
    alergias = models.TextField(blank=True, null=True)  # Alergias conocidas del paciente
    medicamentos_habituales = models.TextField(blank=True, null=True)  # Medicamentos que el paciente toma regularmente

    #signos vitales
    presion_arterial = models.CharField(max_length=7)  # Presión arterial (e.g., "120/80")
    frecuencia_cardiaca = models.IntegerField()  # Frecuencia cardíaca en pulsaciones por minuto
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)  # Temperatura corporal en grados Celsius
    frecuencia_respiratoria = models.IntegerField()  # Frecuencia respiratoria por minuto

    #datos de seguimiento
    proximas_consultas = models.DateField(blank=True, null=True)  # Fecha de la próxima consulta si es aplicable
    recomendaciones = models.TextField(blank=True, null=True)  # Recomendaciones adicionales del doctor

    def __str__(self):
        #muestra el paciente y el doctor cuando se visualiza el objeto
        return f"Historia de {self.paciente.username} atendido por el Dr. {self.doctor.username}"
