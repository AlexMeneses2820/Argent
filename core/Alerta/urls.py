from django.urls import path
from core.Alerta.views.Alerta.views import *

urlpatterns = [
    path('Alerta/', AlertaListview.as_view(), name='Alerta'),
]