from django.urls import path
from .views import *

urlpatterns = [

path("", inicio, name = "inicio"),
path("cursos/", cursos, name = "cursos"),
path("profesores/", profesores, name = "profesores"),
path("estudiantes/", estudiantes, name = "estudiantes"),
path("buscarCurso/", buscarCurso, name = "buscarCurso"),  
path("buscar/", buscar, name = "buscar"), 

]