from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *

from core.Alerta.form import AlertaForm
from core.Alerta.models import Alerta

class AlertaListview(ListView):
    template_name = 'Alerta/productos.html'
    sucess_url = reverse_lazy('Alerta')
    model = Alerta

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user_creation_id=user)

    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        context['Alerta_url'] = reverse_lazy('Alerta')
        return context

class AlertasCreateView(CreateView):
    model = Alerta
    form_class = AlertaForm
    template_name = 'Alerta/Create.html'
    success_url = reverse_lazy('Alerta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añadir una Alerta'
        return context

class AlertaDeleteView(DeleteView):
    model = Alerta
    template_name = 'Alerta/delete.html'
    success_url = reverse_lazy('Alerta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Eliminar Alerta'
        return context