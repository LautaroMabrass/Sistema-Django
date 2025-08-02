from django.db import models

# Tabla clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

# Tabla Articulos
class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

# Tabla de pedidos
class Pedidos (models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
