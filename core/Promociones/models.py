from crum import get_current_user
from django.db import models
from datetime import datetime

from app.settings import MEDIA_URL, STATIC_URL
from core.Categorias.models import Producto2
from core.models import BaseModel


class Promociones(BaseModel):
    Productos = models.ForeignKey(Producto2, blank=True, null=True, on_delete=models.CASCADE)
    Precio = models.DecimalField(default=0, max_digits=9, decimal_places=2,null=True)
    Descuento = models.DecimalField(default=0, max_digits=9, decimal_places=0,null=True)
    imagen = models.ImageField(upload_to='Producto/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Productos

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Promociones, self).save()

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL,'img/Base.jpg')

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'
        ordering = ['id']