from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm

from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "Departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    """
    Crea un nuevo dpto
    """
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short']
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)