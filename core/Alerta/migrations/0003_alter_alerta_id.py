# Generated by Django 3.2.6 on 2021-10-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerta', '0002_auto_20210930_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
