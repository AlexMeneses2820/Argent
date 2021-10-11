from django.forms import ModelForm, TextInput

from core.Alerta.models import Alerta


class AlertaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model= Alerta
        fields='__all__'
        widgets = {
            'Cantidad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Cantidad de Productos',
                    'autocomplete':'off'
                }
            ),
        }
        exclude = ['user_creation', 'date_updated']
