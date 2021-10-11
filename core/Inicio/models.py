from crum import get_current_user
from django.db import models
from datetime import datetime

from core.models import BaseModel


class Cargos(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Cargo', unique=True)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creacion')
    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Cargos, self).save()

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']

class Estado(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Estado')
    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Estado, self).save()

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estado'
        ordering = ['id']

class Empleados(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombres', unique=True)
    Cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='fecha de ingreso')
    date_creation = models.DateTimeField(auto_now=True)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Empleados, self).save()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'
        ordering = ['id']

