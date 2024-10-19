from django.contrib import admin
from .models import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)


class PacienteProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellido', 'numero_seguro_social')


