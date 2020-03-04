from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index.as_view(), name='index'),
    path('consultar/', Consultar_Producto.as_view(), name = 'consultar_producto'),
    path('consultaCart/',Consultar_Carrito.as_view(),name= 'consultar_carrito'),
    path('cesta/<int:pk>', Carrazo.as_view(),name= 'cesta'),

    
]
