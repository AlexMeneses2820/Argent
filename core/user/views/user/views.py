from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.user.forms import RegistroUsuariosForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from core.user.models import User


# Create your views here.

class RegistroCreateView(CreateView):
    model = User
    form_class = RegistroUsuariosForm
    template_name = 'user/registro.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de usuario'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inicio')
        return context

class UsuarioUpdateView(UpdateView):
    model = User
    form_class = RegistroUsuariosForm
    template_name = 'user/Editar.html'
    success_url = reverse_lazy('Perfil')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar usuario'
        context['list_url'] = reverse_lazy('Perfil')
        context['action'] = 'edit'
        return context