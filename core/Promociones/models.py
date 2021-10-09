from django.db import models
from datetime import datetime
from core.Categorias.models import *
class Promociones(models.Model):
    Producto = models.ForeignKey(Producto2, on_delete=models.CASCADE)
    Precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio_despues = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Descuento = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='Producto/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Producto

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'
        ordering = ['id']