from django.shortcuts import render,redirect
from django.views.generic import View,ListView,TemplateView,CreateView
from django.urls import reverse_lazy
#from .forms import EstudianteForm
from .models import Masculino

# Create your views here.
class index(TemplateView):
    template_name = 'p2pApp/index.html'