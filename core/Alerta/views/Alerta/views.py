from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Alerta.models import Alerta

class AlertaListview(ListView):
    template_name = 'Alerta/productos.html'
    sucess_url = reverse_lazy('Alerta')
    model = Alerta

    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        context['Alerta_url'] = reverse_lazy('Alerta')
        return context
