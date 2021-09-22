from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Notificaciones.models import Notificaciones


class NotificacionesListview(ListView):
    template_name = 'Notificaciones/Notificacion.html'
    model = Notificaciones
    sucess_url = reverse_lazy('Notificaciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Notificaciones_url'] = reverse_lazy('Notificaciones')
        return context
