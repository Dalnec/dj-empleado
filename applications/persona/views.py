from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado
#Importa los campos de forms.py de la app
from .forms import EmpleadoForm
# Create your views here.


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'
    
class ListAllEmpleados(ListView):
    """
    Lista todos los empleados
    """
    template_name = 'persona/list_all.html'
    paginate_by = 4 #paginacion para limitar la cantidad de datos a mostrar
    ordering = 'first_name'
    # model = Empleado
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave #icontains busca segun los caracteres que se escriba
        )
        return lista
    
class ListEmpleadosAdmin(ListView):
    """
    Lista todos los empleados
    """
    template_name = 'persona/lista_empleado.html'
    paginate_by = 4 #paginacion para limitar la cantidad de datos a mostrar
    ordering = 'id'
    # model = Empleado
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleados(ListView):
    """
    Lista empleados por departamento
    """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    # queryset = Empleado.objects.filter(
    #     departamento__name = 'Otro'
    # )
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            # departamento__name = 'Otro'
            departamento__name = area
        )
        return lista

class ListEmpleadosByKword(ListView):
    """
    Lista Empleados por palabra clave
    """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            # departamento__name = 'Otro'
            first_name = palabra_clave
        )
        print(lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    """
    Lista las habilidades
    """
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")    
        print(palabra_clave)
        if palabra_clave == '':
            return []
        else:
            empleado = Empleado.objects.get(id=palabra_clave)
            return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del Mes'
        return context


class SuccessView(TemplateView): #Es un template basico Emite un mensaje
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar'] # carga los campos selecionados para el formulario
    # fields = ('__all__')# carga todos los campos
    # success_url = '.' #Para que redireccione a la misma pagina despues de presionar el btn agregar
    # success_url = '/success' #Redirecciona a success.html
    success_url = reverse_lazy('persona_app:empleado_admin') #metodo de django para redirecionar
    
    def form_valid(self, form):
        empleado = form.save(commit=False) #asigna todos los valores guardados del formulario en la variable empleado
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    success_url = reverse_lazy('persona_app:empleado_admin') #metodo de django para redirecionar despues de hacer un post
    
    def post(self, request, *args, **kwargs): # podemos usar metodo post para guardar datos antes de ser validados por el form_valid que POST se ejecuta primero
        """
        request pueder ser usado para recuperar datos enviado por el POST
        """
        self.object = self.get_object()
        # print(request.POST)
        # print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    # def form_valid(self, form): #
    #     return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleado_admin') #metodo de django para redirecionar