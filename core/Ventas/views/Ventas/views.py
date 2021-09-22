from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Ventas.models import Ventas


class VentaListview(ListView):
    template_name = 'Ventas/ventas.html'
    model = Ventas
    sucess_url = reverse_lazy('Ventas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Ventas_url'] = reverse_lazy('Ventas')
        return context
