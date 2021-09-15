from django.forms import *

from core.Inico.models import Empleados


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



        }