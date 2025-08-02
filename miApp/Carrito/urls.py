from django.urls import path
from Carrito import views

urlpatterns = [
        path('', views.carrito, name = 'carrito'),
        path('compra/', views.compra, name = 'compra'),
        path('agregarProductoCarrito/<int:producto_id>', views.agregarProductoCarrito, name = "agregarProductoCarrito"),
        path('eliminarProductoCarrito/<int:producto_id>', views.eliminarProductoCarrito, name = "eliminarProductoCarrito"),
        path('quitarProductoCarrito/<int:producto_id>', views.quitarPorductosCarrito, name = "quitarProductoCarrito"),
        path('vacairProductoCarrito/', views.vaciarCarroCarrito, name = "vaciarCarroCarrito"),
]