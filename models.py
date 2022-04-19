from django.db import models

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50, verbose_name='La dirección')
    email=models.EmailField(blank=True,null=True)
    tfno=models.CharField(max_length=9)

class Productos(models.Model):
    producto=models.CharField(max_length=20)

class cliente_producto (models.Model):
    idcliente=models.IntegerField()
    idproducto=models.IntegerField()

class Meta:
    db_table='clientes'