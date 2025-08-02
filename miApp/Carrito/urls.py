from django.urls import path
from Carrito import views

urlpatterns = [
        path('compra/', views.compra, name = 'compra'),
        path('', views.carrito, name = 'carrito'),
]