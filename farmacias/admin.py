from django.contrib import admin
from .models import Farmacia, Producto

# Registra el modelo Farmacia en el panel de administración de Django
admin.site.register(Farmacia)

# Registra el modelo Producto en el panel de administración de Django
admin.site.register(Producto)
