from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Tipo_Negocio(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        

class Negocio(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    tipo_Negocio=models.ForeignKey(Tipo_Negocio,on_delete=models.PROTECT)
    imagen = models.ImageField(blank='', default = '',upload_to="negocios/")
    creado = models.DateTimeField(auto_now_add=True)
    ubicacion = models.TextField(null = True)
    dueno = models.ForeignKey(User, on_delete=models.CASCADE,related_name="negocios")

    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.IntegerField()
    nuevo=models.BooleanField()
    imagen = models.ImageField(blank='', default = '',upload_to="negocios/items/")
    creado = models.DateTimeField(auto_now_add=True)
    negocio=models.ForeignKey(Tipo_Negocio,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre