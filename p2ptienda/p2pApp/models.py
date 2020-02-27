from django.db import models

# Create your models here.

class Categoria(models.Model):
    nomCat = models.CharField(max_length=70)

    def __str__(self):
        return self.nomCat

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250,null=True)
    fkCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null= True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


