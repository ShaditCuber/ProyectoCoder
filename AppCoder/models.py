from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre  = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + str(self.comision)

#creamos clase estudiante
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

#creamos clase profesor
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + " " + self.apellido+" "+self.profesion

#creamos clase entregable
class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_entrega=models.DateField()
    entregado =models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + " " + str(self.fecha_entrega) + " " + str(self.entregado)
       

class Imagenes(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='imagenes', null=True) 

    def __str__(self):
        return self.nombre