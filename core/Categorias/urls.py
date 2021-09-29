from django.urls import path
from core.Categorias.views.views import *

urlpatterns = [
    path('Categoria/', CategoriaListview.as_view(), name='Categoria'),
    path('Añadir_categoria/', CategoriaCreateView.as_view(), name='Editar'),
    path('Editar_Categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='Editar2'),
    path('Eliminar_Categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='Delete_categoria'),
]