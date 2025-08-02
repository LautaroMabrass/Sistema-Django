from django.shortcuts import render

# Carrito vista
def carrito(request):
    return render(request, 'carrito.html')

# Productos vista
def productos(request):
    return render(request, 'productos.html')
