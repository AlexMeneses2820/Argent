from audioop import add

from crum import get_current_user
from django.db import models
from datetime import datetime

from core.Categorias.models import Producto2
from core.models import BaseModel


class Alerta(BaseModel):
    Cantidad = models.DecimalField(default=0, max_digits=9, decimal_places=2,null=True)
    Producto = models.ForeignKey(Producto2, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Producto

    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
            super(Alerta, self).save()


    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['id']