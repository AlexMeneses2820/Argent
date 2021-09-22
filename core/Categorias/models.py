from django.db import models
from datetime import datetime

class Categorias(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Categorias',unique=True)
    image = models.ImageField(upload_to='Imagen/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']