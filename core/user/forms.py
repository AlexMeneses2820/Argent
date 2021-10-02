from django.contrib.auth.forms import UserCreationForm
from core.user.models import User


class RegistroUsuariosForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email','image',
        labels = {
            'image':'Imagen de perfil (opcional)'
        }

