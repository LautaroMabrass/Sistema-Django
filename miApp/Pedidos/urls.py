from django.urls import path
from Pedidos import views

urlpatterns = [
        path('verificar/', views.verificarCompra, name='verificar'),
        path('confirmado/<int:pedido_id>/', views.confirmado, name='confirmado'),
        path('negado/', views.negado, name='negado'),
        path('historico/', views.historico, name='historico'),
        path('cancelar<int:pedido_id>', views.cancelar, name='cancelar')
]