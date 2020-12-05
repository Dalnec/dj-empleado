from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=100)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = 'Mi Departamento' #cambia el nombre de un titulo en el administrador
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name'] #ordena los items por nombre o segun el orden en la lista ['id', '-name']
        unique_together = ('name', 'short_name') # para no registrar datos repetidos
        
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name