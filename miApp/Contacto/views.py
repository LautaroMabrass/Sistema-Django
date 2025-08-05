from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
# Create your views here.

# Contacto vista
@login_required(login_url='/login/')
def contacto(request):
    formulario_contacto = ContactoForm()

    if request.method == 'POST':
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            mensaje = request.POST.get("mensaje")
            mail = request.user.email
            email = EmailMessage(
                subject="Contacto",
                body=f'Mensaje de {nombre}: \n {mensaje}',
                from_email=mail,
                to=["appwebmail2025@gmail.com"],
            )
            try:
                email.send()
                return redirect('/contacto/?valido')
            except Exception as e:
                print("Error al enviar:", e)
                return redirect('/contacto/?novalido')
    return render(request, 'contacto.html', {"formulario": formulario_contacto})