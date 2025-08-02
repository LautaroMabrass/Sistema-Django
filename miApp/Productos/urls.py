from django.urls import path
from Productos import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('agregar/<int:producto_id>/', views.agregarProducto, name='agregarProducto'),
    path('quitar/<int:producto_id>/', views.quitarPorductos, name='quitarProducto'),  # Corregido
    path('eliminar/<int:producto_id>/', views.eliminarProducto, name='eliminarProducto'),  # Corregido
    path('vaciar/', views.vaciarCarro, name='vaciarCarro')  # vaciar no necesita producto_id
]
