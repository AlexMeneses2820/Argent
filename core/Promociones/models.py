from django.db import models
from datetime import datetime
from core.Categorias.models import Categorias
class Promociones(models.Model):
    Nombre = models.CharField(max_length=150, verbose_name='Nombre de producto',unique=True)
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    Precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Descuento = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Producto = models.ImageField(upload_to='Producto/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'
        ordering = ['id']