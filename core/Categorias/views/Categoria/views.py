from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.Categorias.forms import CategoriaForm, ProductosForm
from core.Categorias.models import Categorias, Producto2


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


#Productos
class ProductoListview(ListView):
    model = Producto2
    template_name = 'Categoria/Productos.html'
    success_url = reverse_lazy('Categoria')



    def get_queryset(self):
        id = self.kwargs['pk']
        return super().get_queryset().filter(category_id = id)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añade un producto nuevo'
        return context

class ProductoDeleteView(DeleteView):
    model = Producto2
    template_name = 'Categoria/delete2.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Eliminar Producto'
        return context

class ProductoUpdateView(UpdateView):
    model = Producto2
    form_class = ProductosForm
    template_name = 'Categoria/Producto_Create.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Editar Producto'
        context['action']= 'Editar'
        return context

class ProductoCreateView(CreateView):
    model = Producto2
    form_class = ProductosForm
    template_name = 'Categoria/Producto_Create.html'
    success_url = reverse_lazy('Categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añadir un Producto Nuevo'
        return context