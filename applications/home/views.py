from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen.html'    

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    # fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'#lleva a la pagina principal o de inicio
