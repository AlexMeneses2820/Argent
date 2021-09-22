from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Perfil.models import Perfil


class PerfilListview(ListView):
    template_name = 'Perfil/perfil.html'
    model = Perfil
    sucess_url = reverse_lazy('Perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Perfil_url'] = reverse_lazy('Perfil')
        return context
