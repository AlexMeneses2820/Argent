from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from core.Notificaciones.models import Notificaciones


class NotificacionesListview(ListView):
    template_name = 'Notificaciones/Notificacion.html'
    model = Notificaciones
    sucess_url = reverse_lazy('Notificaciones')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Notificaciones_url'] = reverse_lazy('Notificaciones')
        return context
