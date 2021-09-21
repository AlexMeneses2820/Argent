from django.forms import *

from core.Inicio.models import Empleados, Cargos


class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Hacer herencia
        #for form in self.visible_fields():
         #   form.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model= Empleados
        fields='__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplate':'off'
                }
            ),
        },

class CargosForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model= Cargos
        fields='__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nuevo Cargo',
                    'autocomplate':'off'
                }
            ),
        },