from django import forms

class NewDepartamentoForm(forms.Form):
    """
    Creando formulario que no se realaciona a ningun modelo(BD)
    """
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    short = forms.CharField(max_length=20)