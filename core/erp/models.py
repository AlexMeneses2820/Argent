from django.db import models
from datetime import datetime

class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creacion')
    image = models.ImageField(upload_to='Categoria/%y/m/%d', null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']



class product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='producto/%y/m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres')
    surname = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    Email = models.CharField(max_length=150, null=True,blank=True,verbose_name='Correo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    sub_total = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    def __str__(self):
        return self.cli.name

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class datesale(models.Model):
    sale = models.ForeignKey(sale,on_delete=models.CASCADE)
    prod = models.ForeignKey(product,on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField (default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'descuento'
        verbose_name_plural = 'descuentos'
        ordering = ['id']
