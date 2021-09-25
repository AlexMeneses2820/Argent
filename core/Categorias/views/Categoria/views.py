from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.Categorias.forms import CategoriaForm
from core.Categorias.models import Categorias


def Categoria_list(request):
    datos={
        'Categoria': Categorias.objects.all()
    }
    return render(datos,'Categoria/lista.html',request)

class CategoriaListview(ListView):
    template_name = 'Categoria/categoria.html'
    model = Categorias
    sucess_url = reverse_lazy('Categoria')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categoria de productos'
        context['Categoria_url'] = reverse_lazy('Categoria')
        context['edit_url'] = reverse_lazy('Editar')
        return context

class CategoriaCreateView(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'Categoria/Create.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añadir Categoria'
        return context

class CategoriaUpdateView(UpdateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'Categoria/Create.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Editar Categorias'
        context['action']= 'Editar'
        return context

class CategoriaDeleteView(DeleteView):
    model = Categorias
    template_name = 'Categoria/delete.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Eliminar Categoria'
        return context
