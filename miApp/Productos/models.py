from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    creacionFecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'CategoriaProducto'
        verbose_name_plural = 'CategoriasProducto'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    url = models.ImageField(upload_to='tienda')
    precio = models.FloatField()
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre