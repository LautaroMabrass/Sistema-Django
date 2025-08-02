from django.shortcuts import render

# Create your views here.

# Login vista
def login(request):
    return render(request, 'login.html')

# Register vista
def register(request):
    return render(request, 'register.html')