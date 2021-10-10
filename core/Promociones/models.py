from django.db import models
from datetime import datetime
from core.Categorias.models import *
class Promociones(models.Model):
    Productos = models.ForeignKey(Producto2, blank=True, null=True, on_delete=models.CASCADE)
    Precio = models.DecimalField(default=0, max_digits=9, decimal_places=2,null=True)
    Descuento = models.DecimalField(default=0, max_digits=3, decimal_places=2,null=True)
    imagen = models.ImageField(upload_to='Producto/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Productos

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL,'img/Base.jpg')

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'
        ordering = ['id']