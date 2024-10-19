
from django.contrib.auth.models import User, Group, Permission
from django.db import models


class Persona(models.Model):
    # Relacionando con el modelo User
    user = models.OneToOneField(User, related_name='%(class)s_profile', on_delete=models.CASCADE, null = True)

    # Relacionando con el modelo Group
    groups = models.ManyToManyField(Group, related_name='%(class)s_profiles', blank=True)

    # Relacionando con el modelo Permission
    user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_permissions', blank=True)

    # Otros campos comunes para doctores y pacientes
    first_name = models.CharField(max_length=100, default='Jhon')
    last_name = models.CharField(max_length=100, default='Smith')
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True
