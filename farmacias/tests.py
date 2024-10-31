from django.test import TestCase
from .models import Farmacia, Producto

# Prueba unitaria para el modelo Farmacia
class FarmaciaModelTest(TestCase):
    def setUp(self):
        # Crea una instancia de Farmacia para pruebas
        self.farmacia = Farmacia.objects.create(nombre="Farmacia Central", direccion="Av. Siempre Viva", telefono="123456789")

    def test_farmacia_creation(self):
        # Verifica que el nombre de la farmacia creada sea el esperado
        self.assertEqual(self.farmacia.nombre, "Farmacia Central")

# Prueba unitaria para el modelo Producto
class ProductoModelTest(TestCase):
    def setUp(self):
        # Crea una instancia de Farmacia y un Producto asociado para pruebas
        farmacia = Farmacia.objects.create(nombre="Farmacia Central", direccion="Av. Siempre Viva", telefono="123456789")
        self.producto = Producto.objects.create(farmacia=farmacia, nombre="Ibuprofeno", precio=10.50, stock=20)

    def test_producto_creation(self):
        # Verifica que el nombre del producto creado sea el esperado
        self.assertEqual(self.producto.nombre, "Ibuprofeno")
