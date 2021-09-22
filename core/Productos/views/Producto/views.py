from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Productos.models import Producto


class ProductoListview(ListView):
    template_name = 'Producto/'
    model = Producto
    sucess_url = reverse_lazy('Producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Producto_url'] = reverse_lazy('Producto')
        return context
