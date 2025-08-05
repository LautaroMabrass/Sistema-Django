from django.shortcuts import render, redirect
from .models import Pedido, LineaPedido
from Carrito.carro import Carro
from Productos.models import Producto
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
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

    productos = []
    for producto_id, datos in carro.carro.items():
        producto = Producto.objects.get(id=producto_id)
        productos.append(f"- {producto.nombre} x {datos['cantidad']}")
    email = EmailMessage(
        subject=f"PEDIDO NUMERO {pedido.id}",
        body=f"Nuevo pedido de {request.user.username}:\n\n" + "\n".join(productos),
        from_email=request.user.email,
        to=["appwebmail2025@gmail.com"],
    )
    try:
        email.send()
    except Exception as e:
        print("Error al enviar:", e)
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