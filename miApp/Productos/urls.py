from django.urls import path
from Productos import views

urlpatterns = [
        path('', views.productos, name = 'productos'),
]