from django.db import models
from datetime import datetime

class Alerta(models.Model):
    Emergencia = models.CharField(max_length=200, verbose_name='Emergencia', unique=True)
    Advertencia = models.CharField(max_length=200, verbose_name='Advertencia',unique=True)
    Aviso = models.CharField(max_length=200, verbose_name='Aviso', unique=True)
    def __str__(self):
        return self.Emergencia

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['id']