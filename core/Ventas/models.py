from django.db import models
from datetime import datetime

class Ventas(models.Model):
    Ventas = models.ImageField(upload_to='Ventas/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Ventas

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
