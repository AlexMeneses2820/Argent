from django.urls import path
from core.Promociones.views.Promociones.views import *

urlpatterns = [
    path('Promociones/', PromocionesListview.as_view(), name='Promociones'),
    path('Crear_Promociones/', PromocionCreateView.as_view(), name='Crear_Promociones'),
]