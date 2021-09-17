"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from core.erp.views import Azucar, Bienvenida, cambiarcontraseña, Carnes, Categorias, Chat, Contacto, \
    EditarPerfil, Frutas, Granos, Iniciar_seccion, Lacteos, Notificaciones, Olvide_contraseña, Perfil, Productos, \
    Promociones, Refrescos, Registro, Venta
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.Inico.urls')),
    path('Bienvenida/', Bienvenida),
    path('cambiarcontraseña/', cambiarcontraseña),
    path('Carnes/', Carnes),
    path('Azucar/', Azucar),
    path('Chat/', Chat),
    path('Contacto/', Contacto),
    path('EditarPerfil/', EditarPerfil),
    path('Frutas/', Frutas),
    path('Granos/', Granos),
    path('Iniciar_seccion/', Iniciar_seccion),
    path('Lacteos/', Lacteos),
    path('Notificaciones/', Notificaciones),
    path('Olvide_contraseña/', Olvide_contraseña),
    path('Perfil/', Perfil),
    path('Productos/', Productos),
    path('Promociones/', Promociones),
    path('Refrescos/', Refrescos),
    path('Registro/', Registro),
    path('Venta/', Venta),
    path('category/', Categorias),
]
