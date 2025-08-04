from django.db import models
from django.contrib.auth import get_user_model
from Productos.models import Producto
from django.db.models import F, Sum, FloatField, ExpressionWrapper

# Create your models here.
USER = get_user_model()

class Pedido (models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    @property
    def total(self):
        total = self.lineapedido_set.aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('precio') * F('cantidad'),
                    output_field=FloatField()
                )
            )
        )['total']
        return total
    
    def __str__(self):
        return f"Pedido #{self.id}"


class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) 

    class Meta:
        verbose_name = 'Línea de Pedido'
        verbose_name_plural = 'Líneas de Pedido'
    

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
