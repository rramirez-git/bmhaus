# Generated by Django 2.0.7 on 2018-10-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('initsys', '0005_auto_20181024_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('idaccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['flujo', 'nombre', 'idaccion'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idestado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('no_estado', models.PositiveSmallIntegerField(default=0)),
                ('es_inicial', models.BooleanField(default=False)),
                ('es_final', models.BooleanField(default=False)),
                ('es_cancelacion', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['flujo', 'no_estado', 'idestado'],
            },
        ),
        migrations.CreateModel(
            name='Flujo',
            fields=[
                ('idflujo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='InstanciaFlujo',
            fields=[
                ('idinstanciaflujo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_instancia', models.CharField(max_length=250)),
                ('terminado', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('estado_actual', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instancias_en_estado', to='flujo.Estado')),
                ('flujo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instancias', to='flujo.Flujo')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['flujo', 'tipo_instancia', 'idinstanciaflujo'],
            },
        ),
        migrations.CreateModel(
            name='InstanciaHistoria',
            fields=[
                ('idinstanciahistoria', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instancias_aplicadoras', to='flujo.Accion')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('instanciaflujo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historia', to='flujo.InstanciaFlujo')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['instanciaflujo', 'accion', 'idinstanciahistoria'],
            },
        ),
        migrations.CreateModel(
            name='InstanciaHistoriaDetalle',
            fields=[
                ('idinstanciahistoriadetalle', models.AutoField(primary_key=True, serialize=False)),
                ('iddocumento_generado', models.CharField(max_length=250)),
                ('tipo_documento_generado', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('instanciahistoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historia_detalle', to='flujo.InstanciaHistoria')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['instanciahistoria', 'tipo_documento_generado', 'iddocumento_generado', 'idinstanciahistoriadetalle'],
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='flujo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estados', to='flujo.Flujo'),
        ),
        migrations.AddField(
            model_name='estado',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
        migrations.AddField(
            model_name='accion',
            name='estado_final',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_ejecutadas', to='flujo.Estado'),
        ),
        migrations.AddField(
            model_name='accion',
            name='estado_inicial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_ejecutar', to='flujo.Estado'),
        ),
        migrations.AddField(
            model_name='accion',
            name='flujo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones', to='flujo.Flujo'),
        ),
        migrations.AddField(
            model_name='accion',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
    ]
