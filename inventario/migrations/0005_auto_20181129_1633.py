# Generated by Django 2.0.7 on 2018-11-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20181128_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendecompra',
            name='identificador',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordendeentrada',
            name='identificador',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
