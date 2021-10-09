from django.forms import *

from core.Categorias.models import Categorias, Producto2


class CategoriaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model= Categorias
        fields='__all__'
        widgets = {
            'Nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Categoria',
                    'autocomplete':'off'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

class ProductosForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model= Producto2
        fields='__all__'
        widgets = {
            'Nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Producto',
                    'autocomplete':'off'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']