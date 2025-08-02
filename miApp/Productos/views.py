from django.shortcuts import render,redirect
from .models import Producto, CategoriaProducto
from Carrito.carro import Carro
# Create your views here.

# Productos vista
def productos(request):
    productos = Producto.objects.all()
    carro = request.session.get("carro", {})
    return render(request, 'productos.html', {"productos": productos, "carro": carro})

def agregarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregarProductos(producto)
    return redirect("productos")


def quitarPorductos(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.quitarProducto(producto)
    return redirect("productos")


def eliminarProducto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminarProducto(producto)
    return redirect("productos")


def vaciarCarro(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect("productos")