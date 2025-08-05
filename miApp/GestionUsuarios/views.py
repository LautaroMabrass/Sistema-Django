from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm 

# Create your views here.

# Register vista
class vistaRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, 'register.html', {"form": form})

# Login vista
def vistaLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm() 

    return render(request, 'login.html', {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')