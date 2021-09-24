from django.db import models
from datetime import datetime

class Perfil(models.Model):
    Descripcion = models.CharField(max_length=300, verbose_name='Descripcion')
    Educacion = models.CharField(max_length=100, verbose_name='Educacion')
    Habilidades = models.CharField(max_length=200, verbose_name='Habilidades')
    Notas = models.CharField(max_length=200, verbose_name='Notas')
    Localizacion = models.CharField(max_length=100, verbose_name='Localizacion')
    Correo = models.CharField(max_length=150, verbose_name='Correo')
    image = models.ImageField(upload_to='Categoria/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Descripcion

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']
