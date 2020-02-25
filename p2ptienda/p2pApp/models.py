from django.db import models

# Create your models here.
class Masculino(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250,null=True)

class Femenino(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250,null=True)

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250,null=True)
    #fktipo

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)

class Categoria(models.Model):
    nomCat = models.CharField(max_length=70)
    tipoCar = ["Ropa","Juguetes","Condones","Lubricantes"]
    #fkProducto
    #fkmasculino
    #fkfemenino