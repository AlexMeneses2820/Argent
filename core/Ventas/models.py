from django.db import models
from datetime import datetime

class Ventas(models.Model):
    date_joined = models.DateField(default=datetime.now)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    def __str__(self):
        return self.Ventas

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
