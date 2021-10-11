from crum import get_current_user
from django.db import models
from app.settings import MEDIA_URL, STATIC_URL
from datetime import datetime

from core.models import BaseModel


class Categorias(BaseModel):
    Nombre = models.CharField(max_length=100, verbose_name='Categorias',unique=True)
    image = models.ImageField(upload_to='Imagen/%y/%m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user

        super(Categorias, self).save()
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL,'img/Base.jpg')
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto2(BaseModel):
    Nombre = models.CharField(max_length=200, verbose_name='Producto', unique=True)
    imagen = models.ImageField(upload_to='imagen/%y/m/%d', null=True, blank=True)
    Cantidad = models.DecimalField(default=0, max_digits=9, decimal_places=2,null=True)
    category = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Producto2, self).save()

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/Base.jpg')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']