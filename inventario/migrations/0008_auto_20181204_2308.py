# Generated by Django 2.0.7 on 2018-12-05 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_auto_20181129_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piezas_ordendeentrada',
            name='ordendeentrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piezas_entradas', to='inventario.OrdenDeEntrada'),
        ),
    ]
