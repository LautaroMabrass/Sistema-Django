from django.shortcuts import render, redirect
from .carro import Carro
from Productos.models import Producto

# Compra vista
def compra(request):
    carro = request.session.get("carro", {})
    items_con_subtotales = []
    total = 0
    for id, item in carro.items():
        subtotal = float(item["cantidad"]) * float(item["precio"])
        total += subtotal
        items_con_subtotales.append({
            "id": id,
            "nombre": item["nombre"],
            "cantidad": item["cantidad"],
            "precio": item["precio"],
            "subtotal": subtotal
        })

    return render(request, 'compra.html', {
        "items": items_con_subtotales, "carro": carro})

# Carrito vista
def carrito(request):
    carro = request.session.get("carro", {})
    return render(request, 'carrito.html', {"carro": carro})

def agregarProductoCarrito(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregarProductos(producto)
    return redirect("carrito")


def quitarPorductosCarrito(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.quitarProducto(producto)
    return redirect("carrito")


def eliminarProductoCarrito(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminarProducto(producto)
    return redirect("carrito")


def vaciarCarroCarrito(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect("carrito")