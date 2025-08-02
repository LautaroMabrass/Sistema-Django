from django.contrib import admin
from .models import CategoriaProducto, Producto
# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("creacionFecha",)

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto)