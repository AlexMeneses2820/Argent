from django.forms import ModelForm, TextInput

from core.Promociones.models import Promociones


class promocionForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model= Promociones
        fields='__all__'
        widgets = {
            'Producto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Cantidad de Productos',
                    'autocomplete':'off'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

