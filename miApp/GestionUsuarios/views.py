from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

# Register vista
class vistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {"form" : form})

    def post(self,request):
        #Obtengo todos los datos del POST
        form = UserCreationForm(request.POST)
        #Almaceno todo en la DB
        usario = form.save()
        return redire

# Login vista
class vistaLogin(View):
    def get(self, request):
        pass

    def post(self,request):
        pass
