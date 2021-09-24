from django.urls import path
from core.Categorias.views.Categoria.views import *

urlpatterns = [
    path('Categoria/', CategoriaListview.as_view(), name='Categoria'),
]