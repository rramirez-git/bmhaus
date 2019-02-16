# Generated by Django 2.0.7 on 2019-01-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfdi', '0004_auto_20181029_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='Descuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='SubTotal',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='Cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='Descuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='Importe',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='ValorUnitario',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='cretencion',
            name='Base',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='cretencion',
            name='Importe',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='cretencion',
            name='TasaOCuota',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='ctraslado',
            name='Base',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='ctraslado',
            name='Importe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='ctraslado',
            name='TasaOCuota',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='impuestos',
            name='TotalImpuestosRetenidos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='impuestos',
            name='TotalImpuestosTrasladados',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='parte',
            name='Cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parte',
            name='Importe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='parte',
            name='ValorUnitario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='retencion',
            name='Importe',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='traslado',
            name='Importe',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
        migrations.AlterField(
            model_name='traslado',
            name='TasaOCuota',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]