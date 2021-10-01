from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def Bienvenida(request):
    return render(request, 'login/Bienvenida.html')

def cambiarcontraseña(request):
    return render(request, 'category/Cargos.html')

def Carnes(request):
    return render(request, 'Carnes.html')

def Azucar(request):
    return render(request, 'Azucares.html')

def Chat(request):
    return render(request, '../Chat/templates/Chat/Chat.html')

def Contacto(request):
    return render(request, '../Contactos/templates/Contactos/Contactos.html')

def EditarPerfil(request):
    return render(request, 'editarPerfil.html')

def Frutas(request):
    return render(request, 'Frutas_y_verduras.html')

def Granos(request):
    return render(request, 'Granos.html')

def Iniciar_seccion(request):
    return render(request, 'iniciar_sesion.html')

def Lacteos(request):
    return render(request, 'Lacteos.html')

def Notificaciones(request):
    return render(request, '../Notificaciones/templates/Notificaciones/Notificacion.html')

def Olvide_contraseña(request):
    return render(request, 'Olvide-contraseña.html')

def  Perfil(request):
    return render(request, '../Perfil/templates/Perfil/perfil.html')

def Productos(request):
    return render(request, '../Alerta/templates/Alerta/productos.html')

def Promociones(request):
    return render(request, '../Promociones/templates/Promociones/Promociones.html')

def Refrescos(request):
    return render(request, 'Refrescos.html')

def Venta(request):
    return render(request, '../Ventas/templates/Ventas/ventas.html')

def Categorias(request):
    return render(request, '../Categorias/templates/Categoria/categoria.html')

def Registro(request):
    return render(request, 'Registro.html')
