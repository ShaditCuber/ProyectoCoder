from django.urls import path
from .views import  *


urlpatterns = [
        #path('curso/', curso),
        #name sirve para llamar a la vista sin url
        path('', inicio, name='inicio'),
        path('cursos/', cursos, name='cursos'),
        path('estudiantes/', estudiantes,name='estudiantes'),
        path('profesores/', profesores,name='profesores'),
        path('entregables/', entregables,name='entregables'),
        #path('cursoFormulario/', cursoFormulario,name='cursoFormulario'),
        #path('profeFormulario/', profeFormulario,name='profeFormulario'),
        path('buscarComision/', buscarComision,name='buscarComision'),
        path('buscar/', buscar,name='buscar'),
        path('imagenes/', imagenes,name='imagenes'),
        path('buscarImagen/', buscarImagen,name='buscarImagen'),
        path('buscarImagens/', buscarImagens,name='buscarImagens'),
        ]