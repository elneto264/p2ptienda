from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView
from django.urls import reverse_lazy
from .forms import ProForm
from .models import *
# Create your views here.

class Inicio(TemplateView):
    template_name = 'p2pApp/index.html'

class Consultar_Producto(ListView):
    model = Producto
    template_name = 'p2pApp/consultaTienda.html'
    context_object_name= 'p2pApp'
    queryset = Producto.objects.all()
    
class Categoria(ListView):
    model = Producto
    listado = Categoria.objects.filter(fk_producto_id=id)
    template_name = 'p2pApp/categoria.html'
    context_object_name= 'p2pApp'
    queryset = Producto.objects.all()


