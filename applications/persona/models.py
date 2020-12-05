from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)    

    class Meta:
        verbose_name = "Habilidades"
        verbose_name_plural = "Habilidadess"

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres Completos',
        max_length = 120,
        blank = True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #clave foranea
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades) # relacion de muchos a muchos
    hoja_de_vida = RichTextField()  #usando app de terceros, editor de texto
    
    class Meta:
        verbose_name = 'Area de Empleado' #cambia el nombre de un titulo en el administrador
        ordering = ['-id'] #ordena los items por nombre o segun el orden en la lista ['id', '-name']
        unique_together = ('first_name', 'last_name', 'job') # para no registrar datos repetidos
        
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name