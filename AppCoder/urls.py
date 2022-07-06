from django.urls import path
from .views import  *


urlpatterns = [
        path('curso/', curso),
        #name sirve para llamar a la vista sin url
        path('', inicio, name='inicio'),
        path('cursos/', cursos, name='cursos'),
        path('estudiantes/', estudiantes,name='estudiantes'),
        path('profesores/', profesores,name='profesores'),
        path('entregables/', entregables,name='entregables'),]