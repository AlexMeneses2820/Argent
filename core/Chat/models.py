from django.db import models
from datetime import datetime

class Chat(models.Model):
    Nombreuser = models.CharField(max_length=150, verbose_name='Nombre de usuario')
    Mensaje = models.CharField(max_length=500, verbose_name='Mensaje')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creacion')
    Imagen = models.ImageField(upload_to='Imagen/%y/m/%d', null=True, blank=True)
    Avatar = models.ImageField(upload_to='Avatar/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.Nombreuser

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        ordering = ['id']