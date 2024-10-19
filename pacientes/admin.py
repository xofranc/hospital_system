from django.contrib import admin
from pacientes.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'seguro_medico')  # Ajusta a campos reales
    search_fields = ('first_name', 'last_name', 'seguro_medico')
    ordering = ('first_name',)
admin.site.register(Paciente, PacienteAdmin)
