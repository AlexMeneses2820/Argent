from django.urls import path
from core.user.views.user.views import RegistroCreateView,UsuarioUpdateView

urlpatterns = [
    path('Registro/', RegistroCreateView.as_view(), name='registro'),
    path('Editar_Usuario/', UsuarioUpdateView.as_view(), name='User_edit'),
]