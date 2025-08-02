from django.shortcuts import render

# Create your views here.

# Productos vista
def productos(request):
    return render(request, 'productos.html')