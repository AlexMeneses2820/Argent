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
from django.urls import path,include

from core.erp.views import Azucar, Bienvenida, cambiarcontraseña, Carnes, Categorias, Chat, Contacto, \
    EditarPerfil, Frutas, Granos, Iniciar_seccion, Lacteos, Notificaciones, Olvide_contraseña, Perfil, Productos, \
    Promociones, Refrescos, Registro, Venta

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.Inicio.urls')),
    path('', include('core.Alerta.urls')),
    path('', include('core.Categorias.urls')),
    path('', include('core.Chat.urls')),
    path('', include('core.Contactos.urls')),
    path('', include('core.Notificaciones.urls')),
    path('', include('core.Perfil.urls')),
    path('', include('core.Promociones.urls')),
    path('', include('core.Ventas.urls')),
    path('', include('core.login.urls')),
    path('', include('core.user.urls')),
    #Ajustes
    path('Carnes/', Carnes),
    path('Azucar/', Azucar),
    path('Frutas/', Frutas),
    path('Granos/', Granos),
    path('Lacteos/', Lacteos),
    path('Refrescos/', Refrescos),
    path('Registro/', Registro),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)