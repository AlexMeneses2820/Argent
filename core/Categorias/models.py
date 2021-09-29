from django.db import models
from app.settings import MEDIA_URL
from datetime import datetime

class Categorias(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Categorias',unique=True)
    image = models.ImageField(upload_to='Imagen/%y/%m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']