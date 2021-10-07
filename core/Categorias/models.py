from django.db import models
from app.settings import MEDIA_URL, STATIC_URL
from datetime import datetime

class Categorias(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Categorias',unique=True)
    image = models.ImageField(upload_to='Imagen/%y/%m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL,'img/None.jpg')
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto2(models.Model):
    Nombre = models.CharField(max_length=200, verbose_name='Producto', unique=True)
    imagen = models.ImageField(upload_to='imagen/%y/m/%d', null=True, blank=True)
    Cantidad = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    category = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre

    def __str__(self):
        return self.Nombre
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/None.jpg')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']