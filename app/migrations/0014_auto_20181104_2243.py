# Generated by Django 2.0.7 on 2018-11-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20181103_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avanceenflujo',
            name='nota',
            field=models.TextField(blank=True, null=True),
        ),
    ]