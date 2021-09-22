from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Promociones.models import Promociones


class PromocionesListview(ListView):
    template_name = 'Promociones/Promociones.html'
    model = Promociones
    sucess_url = reverse_lazy('Promociones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Promociones_url'] = reverse_lazy('Promociones')
        return context
