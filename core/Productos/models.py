from django.db import models
from datetime import datetime

class Producto(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name='Producto', unique=True)
    imagen = models.ImageField(upload_to='imagen/%y/m/%d', null=True, blank=True)
    Cantidad = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
