from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre  = models.CharField(max_length=40)
    comision = models.IntegerField()

#creamos clase estudiante
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

#creamos clase profesor
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

#creamos clase entregable
class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_entrega=models.DateField()
    entregado =models.BooleanField(default=False)
       