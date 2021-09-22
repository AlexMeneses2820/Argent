from django.db import models
from datetime import datetime

class Contactos(models.Model):
    Nombre = models.CharField(max_length=150, verbose_name='Nombre')
    Avatar = models.ImageField(upload_to='Avatar/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['id']
