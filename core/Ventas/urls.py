from django.urls import path
from core.Ventas.views.Ventas.views import *

urlpatterns = [
    path('Ventas/', VentaListview.as_view(), name='Ventas'),
]