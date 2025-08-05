from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-3 shadow-sm',
            'placeholder': 'Tu nombre'
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