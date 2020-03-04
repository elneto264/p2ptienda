from django.urls import path, include
from .views import *
from usuario.views import RegistroUsuario,Login,logoutUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('consultar/', Consultar_Producto.as_view(), name = 'consultar_producto'),
    path('registrar/',RegistroUsuario.as_view(),name='registrar'), 
    path('accounts/login/',Login.as_view(),name ='login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('consultaCart/',Consultar_Carrito.as_view(),name= 'consultar_carrito'),
    path('cesta/<int:pk>', Carrazo.as_view(),name= 'cesta'),

    
]
