from django.urls import path
from core.Productos.views.Producto.views import *

urlpatterns = [
    path('Producto/', ProductoListview.as_view(), name='Producto'),
]