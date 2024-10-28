from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models

class PacienteManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Paciente(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = PacienteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'fecha_nacimiento']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class MedicalInfo(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} - Medical Info"

# logins/models.py

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)  # Puedes crear un ForeignKey a un modelo de Doctor si lo deseas
    date_time = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Cita para {self.patient.username} con {self.doctor} el {self.date_time}"
