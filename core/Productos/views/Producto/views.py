from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from core.Productos.models import Producto


class ProductoListview(ListView):
    template_name = 'Producto/'
    model = Producto
    sucess_url = reverse_lazy('Producto')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Producto_url'] = reverse_lazy('Producto')
        return context
