from django.db import models
from datetime import datetime


class Cargos(models.Model):
    name = models.CharField(max_length=150, verbose_name='Cargo', unique=True)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creacion')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']

class Estado(models.Model):
    name = models.CharField(max_length=150, verbose_name='Estado')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estado'
        ordering = ['id']

class Empleados(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres', unique=True)
    Cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='fecha de ingreso')
    date_creation = models.DateTimeField(auto_now=True)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'
        ordering = ['id']

