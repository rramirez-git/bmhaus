# Generated by Django 2.0.7 on 2018-10-29 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181025_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoordenreparacion',
            name='fecha_y_hora_de_recepcion',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 10, 52, 10, 712490)),
        ),
    ]