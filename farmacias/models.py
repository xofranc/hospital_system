from django.db import models

# Modelo que representa un proveedor en el sistema de farmacia.
class Proveedor(models.Model):
    # Nombre del proveedor
    nombre = models.CharField(max_length=100)
    # Dirección del proveedor
    direccion = models.TextField()
    # Teléfono de contacto del proveedor
    telefono = models.CharField(max_length=15)
    # Email de contacto, debe ser único
    email = models.EmailField(unique=True)

    def __str__(self):
        # Representación en texto del modelo (se muestra en el admin)
        return self.nombre

# Modelo que representa un medicamento.
class Medicamento(models.Model):
    # Nombre del medicamento
    nombre = models.CharField(max_length=100)
    # Descripción breve del medicamento
    descripcion = models.TextField()
    # Precio del medicamento, con dos decimales
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Cantidad disponible en el inventario
    cantidad_disponible = models.IntegerField()
    # Relación de muchos a uno con el modelo Proveedor
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='medicamentos')

    def __str__(self):
        # Representación en texto del medicamento
        return self.nombre

# Modelo que representa a un cliente en el sistema de farmacia.
class Cliente(models.Model):
    # Nombre del cliente
    nombre = models.CharField(max_length=100)
    # Dirección del cliente
    direccion = models.TextField()
    # Teléfono de contacto del cliente
    telefono = models.CharField(max_length=15)
    # Email de contacto, debe ser único
    email = models.EmailField(unique=True)
    # Fecha en que el cliente fue registrado en el sistema
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        # Representación en texto del cliente
        return self.nombre

# Modelo que representa una venta realizada a un cliente.
class Venta(models.Model):
    # Cliente que realizó la compra
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Medicamento comprado por el cliente
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    # Cantidad del medicamento vendido
    cantidad = models.IntegerField()
    # Fecha en que se realizó la venta, asignada automáticamente
    fecha_venta = models.DateTimeField(auto_now_add=True)
    # Total de la venta calculado (cantidad * precio del medicamento)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Representación en texto de la venta
        return f"Venta de {self.cantidad} unidades de {self.medicamento.nombre} a {self.cliente.nombre}"

    def save(self, *args, **kwargs):
        # Sobrescribimos el método save para calcular el total antes de guardar
        self.total = self.cantidad * self.medicamento.precio
        super().save(*args, **kwargs)
 