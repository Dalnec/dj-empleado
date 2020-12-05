from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        # fields = ('__all__')
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese Texto',
                    'class': 'txt'
                }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"] # recupera lo que se escribe en el form html
        if cantidad <10:
            raise forms.ValidationError('Ingrese un numero mayor a 10') #Emite un mensaje si la condicion no cumple en el formulario html, antes de que consulte a la base de datos
        return cantidad