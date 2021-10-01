from django.contrib.auth.forms import UserCreationForm
from core.user.models import User


class RegistroUsuariosForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email','image',
        labels = {
            'image':'Imagen de perfil (opcional)'
        }


    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
