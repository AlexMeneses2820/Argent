from django.urls import path
from core.Notificaciones.views.Notificaciones.views import *

urlpatterns = [
    path('Notificaciones/', NotificacionesListview.as_view(), name='Notificaciones'),
]