from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Inicio.as_view(), name='index'),
    path('consultar/', Consultar_Producto.as_view(), name = 'consultar_producto'),
]
