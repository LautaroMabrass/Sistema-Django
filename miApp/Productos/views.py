from django.shortcuts import render
from .models import Producto, CategoriaProducto
# Create your views here.

# Productos vista
def productos(request):
    productos = Producto.objects.all()

    return render(request, 'productos.html', {"productos": productos})