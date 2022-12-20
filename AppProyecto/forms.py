from django import forms

class CursoForm(forms.Form):
    materia = forms.CharField(label = "Nombre de la materia", max_length = 30)
    comision = forms.IntegerField(label = "Numero de la comision")

class ProfesorForm(forms.Form):
    nombre = forms.CharField(label = "Nombre del profesor",max_length = 20)
    apellido = forms.CharField(label = "Apellido del profesor",max_length = 20)
    materia = forms.CharField(label = "Profesor de que materia es",max_length = 30)
    

class EstudianteForm(forms.Form):
    nombre = forms.CharField(label = "Nombre del alumno",max_length = 20)
    apellido = forms.CharField(label = "Apellido del alumno",max_length = 20)
    legajo = forms.IntegerField(label = "Numero de legajo del alumno")
    