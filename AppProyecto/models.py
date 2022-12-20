from django.db import models

# Create your models here.
class Curso(models.Model):
    materia = models.CharField(max_length = 30)
    comision = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    materia = models.CharField(max_length = 30)
    


class Estudiante(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    legajo = models.IntegerField()
    

