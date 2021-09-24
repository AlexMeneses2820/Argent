from django.urls import path
from core.Perfil.views.Perfil.views import *

urlpatterns = [
    path('Perfil/', PerfilListview.as_view(), name='Perfil'),
]