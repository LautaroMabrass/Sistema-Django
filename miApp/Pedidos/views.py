from django.shortcuts import render, redirect
from .models import Pedido, LineaPedido
from Carrito.carro import Carro
from Productos.models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def verificarCompra(request):
    carro = Carro(request)
    if not carro.carro:
        return redirect('negado')
    
    # Crear pedido para el usuario actual
    pedido = Pedido.objects.create(user=request.user)

    for producto_id, datos in carro.carro.items():
        producto = Producto.objects.get(id=producto_id)
        LineaPedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=datos['cantidad'],
            precio=datos['precio']
        )
    # Vaciar carrito 
    carro.vaciar()
    
    return redirect('confirmado', pedido_id=pedido.id)

# Vista exito
def confirmado(request, pedido_id):
    return render(request, 'exito.html', {'pedido_id': pedido_id})

# Vista error
def negado(request):
    return render(request, 'error.html')

# Vista historico
@login_required(login_url='/login/')
def historico(request):
    pedidos = Pedido.objects.filter(user=request.user).order_by('id')
    return render(request, 'historicoPedidos.html', {'pedidos': pedidos})

@login_required(login_url='/login/')
def cancelar(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.delete()
    return redirect('historico')