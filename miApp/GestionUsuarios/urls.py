from django.urls import path
from GestionUsuarios.views import vistaLogin,vistaRegistro, cerrar_sesion

urlpatterns = [
    path('login/', vistaLogin, name = 'login'),
    path('register/', vistaRegistro.as_view(), name = 'register'),
    path('logout/', cerrar_sesion, name='logout')
]