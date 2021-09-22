from django.db import models
from datetime import datetime

class Notificaciones(models.Model):
    Mensaje = models.CharField(max_length=300, verbose_name='Mensaje')
    Avatar = models.ImageField(upload_to='Avatar/%y/m/%d', null=True, blank=True)
    Imagen = models.ImageField(upload_to='Imagen/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Mensaje

    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        ordering = ['id']
