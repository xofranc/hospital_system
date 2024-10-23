from django.db import models
from common.models import Persona  

class Doctor(Persona):
    license_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Doctor)"