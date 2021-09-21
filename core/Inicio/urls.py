from django.urls import path
from core.Inicio.views.category.views import *
urlpatterns = [
    path('', Category_ListView.as_view(), name='inicio'),
    path('Nuevos_usuarios/', CategoryCreateView.as_view(), name='Nuevo-Usuario'),
    path('Cargos_nuevos/', CagosCreateView.as_view(), name='Cargos'),
]