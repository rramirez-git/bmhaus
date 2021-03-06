from django.db import models

from datetime import datetime

from initsys.models import Usr, Direccion

# Create your models here.


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=254, null=True, blank=True)
    rfc = models.CharField(max_length=13)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    extension = models.CharField(max_length=5, null=True, blank=True)
    direccion = models.ForeignKey(
        Direccion, on_delete=models.PROTECT,
        related_name="proveedor")
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.razon_social

    def __unicode__(self):
        return self.__str__()


class Pieza(models.Model):
    idpieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    precio = models.DecimalField(
        max_digits=13, decimal_places=6, default=0.0)
    porcentaje_de_iva = models.DecimalField(
        max_digits=4, decimal_places=2, default=16.0)
    proveedores = models.ManyToManyField(
        Proveedor, through='Proveedor_Piezas',
        through_fields=('pieza', 'proveedor'))
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = self.nombre
        if self.marca:
            name += " " + self.marca
        if self.modelo:
            name += " " + self.modelo
        return name

    def __unicode__(self):
        return self.__str__()


class Proveedor_Piezas(models.Model):
    idproveedor_piezas = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.proveedor, self.pieza)

    def __unicode__(self):
        return self.__str__()


class OrdenDeCompra(models.Model):
    idordendecompra = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT,
        related_name="ordenesdecompra")
    fecha = models.DateField(default=datetime.today)
    piezas = models.ManyToManyField(
        Pieza, through='Piezas_OrdenDeCompra',
        through_fields=('ordendecompra', 'pieza'))
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "({}) {} - {}".format(
            self.idordendecompra, self.proveedor, self.fecha)

    def __unicode__(self):
        return self.__str__()


class Piezas_OrdenDeCompra(models.Model):
    idpiezas_ordendecompra = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    ordendecompra = models.ForeignKey(
        OrdenDeCompra, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=0)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.ordendecompra, self.pieza)

    def __unicode__(self):
        return self.__str__()


class OrdenDeEntrada(models.Model):
    idordendeentrada = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT,
        related_name="ordenesdeentrada")
    fecha = fecha = models.DateField(default=datetime.today)
    piezas = models.ManyToManyField(
        Pieza, through='Piezas_OrdenDeEntrada',
        through_fields=('ordendeentrada', 'pieza'))
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "({}) {} - {}".format(
            self.idordendecompra, self.proveedor, self.fecha)

    def __unicode__(self):
        return self.__str__()


class Piezas_OrdenDeEntrada(models.Model):
    idpiezas_ordendeentrada = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    ordendeentrada = models.ForeignKey(
        OrdenDeEntrada, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=0)
    costo = models.DecimalField(
        max_digits=13, decimal_places=6, default=0.0)
    importe = models.DecimalField(
        max_digits=13, decimal_places=6, default=0.0)
    created_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Usr, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.ordendecompra, self.pieza)

    def __unicode__(self):
        return self.__str__()
