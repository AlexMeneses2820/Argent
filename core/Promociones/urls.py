from django.urls import path
from core.Promociones.views.Promociones.views import *

urlpatterns = [
    path('Promociones/', PromocionesListview.as_view(), name='Promociones'),
    path('Crear_Promociones/', PromocionCreateView.as_view(), name='Crear_Promociones'),
    path('Eliminar_Promociones/<int:pk>/', PromocionDeleteView.as_view(), name='Eliminar_Promociones'),
    path('Editar_Promociones/<int:pk>/', PromocionUpdateView.as_view(), name='Editar_Promociones'),
]