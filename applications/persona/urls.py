from django.contrib import admin
from django.urls import path

# def desdePersona(self):
#     print('desde la app persona=====================')
    
# urlpatterns = [
#     path('persona/', desdePersona)
# ]
from . import views

app_name = "persona_app"

urlpatterns = [
    path( #url para pagina de inicio
        '',
        views.InicioView.as_view(),
        name='Inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-by-area/<shortname>/', 
        views.ListByAreaEmpleados.as_view(),
        name='empleado_areas'
    ),
    path('buscar_empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista_habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
        'update-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado' #etiqueta
    ),
    path(
        'delete-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado' #etiqueta
    ),
    path(
        'lista-empleado-admin',
        views.ListEmpleadosAdmin.as_view(),
        name='empleado_admin' #etiqueta
    ),
]