from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from core.Ventas.models import Ventas


class VentaListview(ListView):
    template_name = 'Ventas/ventas.html'
    model = Ventas
    sucess_url = reverse_lazy('Ventas')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Ventas_url'] = reverse_lazy('Ventas')
        return context
