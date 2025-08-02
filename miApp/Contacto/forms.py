from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-3 shadow-sm',
            'placeholder': 'Tu nombre'
        })
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control rounded-3 shadow-sm',
            'placeholder': 'tu@email.com'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'class': 'form-control rounded-3 shadow-sm',
            'rows': 4,
            'placeholder': 'Escribe tu mensaje...'
        })
    )