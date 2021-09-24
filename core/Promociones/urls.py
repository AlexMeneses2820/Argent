from django.urls import path
from core.Promociones.views.Promociones.views import *

urlpatterns = [
    path('Promociones/', PromocionesListview.as_view(), name='Promociones'),
]