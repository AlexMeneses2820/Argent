from django.urls import path
from core.Alerta.views.Alerta.views import *

urlpatterns = [
    path('Alerta/', AlertaListview.as_view(), name='Alerta'),
    path('Crear_Alerta/', AlertaCreateView.as_view(), name='Crear Alerta'),
    path('Eliminar_Alerta/<int:pk>/', AlertaDeleteView.as_view(), name='Alerta_Delete'),
]