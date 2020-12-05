from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    #full name llama a la funcion y uno dos comlunas en una
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    search_fields = ('first_name',) #agrega un campo de busqueda
    list_filter = ('departamento', 'job', 'habilidades') #genera una lista para filtrar la columna job
    filter_horizontal = ('habilidades',) #genera un filtro para las habilidades al momento de registrar un empleado
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
