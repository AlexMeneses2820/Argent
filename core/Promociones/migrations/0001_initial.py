# Generated by Django 3.2.6 on 2021-10-07 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre de producto')),
                ('Precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Producto', models.ImageField(blank=True, null=True, upload_to='Producto/%y/m/%d')),
                ('Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categorias.categorias')),
            ],
            options={
                'verbose_name': 'Promocion',
                'verbose_name_plural': 'Promociones',
                'ordering': ['id'],
            },
        ),
    ]
