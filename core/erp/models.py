from django.db import models
from datetime import datetime


class datesale(models.Model):
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField (default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'descuento'
        verbose_name_plural = 'descuentos'
        ordering = ['id']
