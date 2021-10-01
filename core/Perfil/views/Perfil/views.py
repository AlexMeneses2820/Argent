from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from core.Perfil.models import PerfilModel


class PerfilListview(ListView):
    template_name = 'Perfil/perfil.html'
    model = PerfilModel
    sucess_url = reverse_lazy('Perfil')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Perfil_url'] = reverse_lazy('Perfil')
        return context
