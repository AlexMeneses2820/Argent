from django.urls import path
from core.Contactos.views.Contactos.views import *

urlpatterns = [
    path('Contactos/', ContactosListview.as_view(), name='Contactos'),
]