from django.shortcuts import render

# Compra vista
def compra(request):
    return render(request, 'carrito.html')

# Carrito vista
def carrito(request):
    return render(request, 'carrito.html')
