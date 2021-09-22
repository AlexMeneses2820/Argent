from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Contactos.models import Contactos


class ContactosListview(ListView):
    template_name = 'Contactos/Contactos.html'
    model = Contactos
    sucess_url = reverse_lazy('Contactos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Contactos_url'] = reverse_lazy('Contactos')
        return context
