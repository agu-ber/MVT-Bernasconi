from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    es_casado = models.BooleanField()