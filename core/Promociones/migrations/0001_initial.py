# Generated by Django 3.2.6 on 2021-10-12 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True)),
                ('Descuento', models.DecimalField(decimal_places=0, default=0, max_digits=9, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Producto/%y/m/%d')),
                ('Productos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Categorias.producto2')),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Promocion',
                'verbose_name_plural': 'Promociones',
                'ordering': ['id'],
            },
        ),
    ]
