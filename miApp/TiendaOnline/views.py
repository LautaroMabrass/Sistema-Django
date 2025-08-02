from django.http import HttpResponse
from django.shortcuts import render

# Index vista
def index(request):
    return render(request, 'index.html')

# Login vista
def login(request):
    return render(request, 'login.html')

# Register vista
def register(request):
    return render(request, 'register.html')

# Contacto vista
def contacto(request):
    return render(request, 'contacto.html')