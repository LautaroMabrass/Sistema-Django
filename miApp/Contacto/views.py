from django.shortcuts import render, redirect
from .forms import ContactoForm
# Create your views here.

# Contacto vista
def contacto(request):
    formulario_contacto = ContactoForm()

    if request.method == 'POST':
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
            return redirect('/contacto/?valido')
    return render(request, 'contacto.html', {"formulario": formulario_contacto})