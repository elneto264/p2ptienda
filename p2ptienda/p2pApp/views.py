from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ProForm, CarroForm
from .models import Categoria, Producto, Carrito
from django.contrib.auth.models import User


# Create your views here.

class index(TemplateView):
    template_name = 'p2pApp/index.html'

class Consultar_Producto(ListView):
    model = Producto
    template_name = 'p2pApp/consultaTienda.html'
    context_object_name= 'p2pApp'
    queryset = Producto.objects.all()

class Consultar_Carrito(ListView):
    model = Carrito
    template_name = 'p2pApp/consultarCarrito.html'
    context_object_name= 'p2pApp'
    queryset = Carrito.objects.all()   

class Carrazo(CreateView):
    model= Carrito
    template_name = 'p2pApp/cestaProduct.html'
    form_class = CarroForm
    success_url = reverse_lazy('p2pApp:consultar_producto')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        producto = Producto.objects.get(pk = self.kwargs.get('pk',None))
        self.object.producto = producto
        usuario = User.objects.get(pk = 1)
        self.object.user = usuario

        self.object.save()
        return super(Carrazo,self).form_valid(form)

class EliminiarCarrito(DeleteView):
    model = Carrito
    success_url= reverse_lazy('p2pApp:consultar_carrito')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PagarCarrito(DeleteView):
    model = Carrito
    #success_url= reverse_lazy('p2pApp:consultar_producto')

    def showthis(request):
        Carrito.objects.all().delete()
        context={}
        return render(request,'p2pApp:consultar_producto',context)





                


    

