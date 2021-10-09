from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *

from core.Promociones.form import promocionForm
from core.Promociones.models import Promociones


class PromocionesListview(ListView):
    template_name = 'Promociones/Promociones.html'
    model = Promociones
    sucess_url = reverse_lazy('Promociones')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Promociones_url'] = reverse_lazy('Promociones')
        return context

class PromocionCreateView(CreateView):
    model = Promociones
    form_class = promocionForm
    template_name = 'Promociones/create.html'
    success_url = reverse_lazy('Promociones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añadir una Promocion'
        return context