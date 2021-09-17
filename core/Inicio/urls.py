from django.urls import path
from core.Inicio.views.category.views import *
urlpatterns = [
    path('', Category_ListView.as_view(), name='inicio'),
    path('add_programdores/', CategoryCreateView.as_view(), name='add_programdores'),
]