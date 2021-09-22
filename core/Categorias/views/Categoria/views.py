from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Categorias.models import Categorias


class CategoriaListview(ListView):
    template_name = 'Categoria/categoria.html'
    model = Categorias
    sucess_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categoria_url'] = reverse_lazy('Categoria')
        return context
