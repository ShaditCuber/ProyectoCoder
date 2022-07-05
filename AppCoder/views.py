from django.http import HttpResponse
#from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.


def curso(self):
    curso = Curso(nombre="Desarrollo Web",comision="19881")
    curso.save()
    documento_de_texto=f"   --->Curso : {curso.nombre} \n Comision: {curso.comision}"
    return HttpResponse(documento_de_texto)