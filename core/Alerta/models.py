from audioop import add

from django.db import models
from datetime import datetime

from core.Categorias.models import Producto2

class Alerta(models.Model):
    Cantidad = models.DecimalField(default=0, max_digits=9, decimal_places=2,null=True)
    Producto = models.ForeignKey(Producto2, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Producto

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['id']