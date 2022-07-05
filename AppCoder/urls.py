from django.urls import path
from .views import  *


urlpatterns = [
        path('curso/', curso),
        path('', inicio),
        path('cursos/', cursos),
        path('estudiantes/', estudiantes),
        path('profesores/', profesores),
        path('entregables/', entregables),]