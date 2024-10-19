from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'especialidad')  # Añade campos reales
    search_fields = ('first_name', 'last_name', 'especialidad')
    ordering = ('first_name',)