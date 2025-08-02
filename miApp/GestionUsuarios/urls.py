from django.urls import path
from GestionUsuarios.views import vistaLogin,vistaRegistro

urlpatterns = [
    path('login/', vistaLogin.as_view(), name = 'login'),
    path('register/', vistaRegistro.as_view(), name = 'register'),
]