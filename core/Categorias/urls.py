from django.urls import path
from core.Categorias.views.Categoria.views import *

urlpatterns = [
    path('Categoria/', CategoriaListview.as_view(), name='Categoria'),
    path('Añadir_categoria/', CategoriaCreateView.as_view(), name='Editar'),
    path('Editar_Categoria/<int:pk>/', CategoriaUpdateView.as_view(), name='Editar2'),
    path('Eliminar_Categoria/<int:pk>/', CategoriaDeleteView.as_view(), name='Delete_categoria'),
    #Producto
    path('Añade_un_producto/<int:pk>/', ProductoListview.as_view(), name='Produ'),
    path('Editar_Producto/<int:pk>/', ProductoUpdateView.as_view(), name='Producto_editar'),
    path('Eliminar_Producto/<int:pk>/', ProductoDeleteView.as_view(), name='Producto_Eliminar'),
    path('Crear_Producto/', ProductoCreateView.as_view(), name='Crear_producto'),
]