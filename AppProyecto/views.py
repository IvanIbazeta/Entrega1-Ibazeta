from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *



# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    if request.method=="POST":
       form = CursoForm(request.POST)
       if form.is_valid():
            info = form.cleaned_data
            materia = info["materia"]
            comision = info["comision"]
            curso = Curso(materia = materia, comision = comision)
            curso.save()
            return render(request, "cursos.html", {"mensaje": "El curso se guardo correctamente"})
       else:
            return render(request, "cursos.html", {"form": form, "mensaje": "La informacion ingresada no es valida"})
    else:
        formulario = CursoForm()   
        return render(request, "cursos.html", {"form": formulario})

def profesores(request):
    if request.method=="POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            materia = info["materia"]
            profesor = Profesor(nombre = nombre, apellido = apellido, materia = materia)
            profesor.save()
            return render(request, "profesores.html", {"mensaje": "El profesor se guardo correctamente"})
        else:
            return render(request, "profesores.html", {"form": form, "mensaje": "La informacion ingresada no es valida"})
    else:
        formulario = ProfesorForm()
        return render(request, "profesores.html", {"form": formulario})

def estudiantes(request):
    if request.method=="POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            legajo = info["legajo"]
            estudiante = Estudiante(nombre = nombre, apellido = apellido, legajo = legajo)
            estudiante.save()
            return render(request, "estudiantes.html", {"mensaje": "El estudiante se guardo correctamente"})
        else:
            return render(request, "estudiantes.html", {"form": form, "mensaje": "La informacion ingresada no es valida"})
    else:
        formulario = EstudianteForm()
        return render(request, "estudiantes.html", {"form": formulario})

def buscarCurso(request):
    return render(request, "buscarCurso.html")

def buscar(request):
    comision = request.GET["comision"]
    if comision!="":
        cursos = Curso.objects.filter(comision__icontains = comision)
        return render(request, "resultadoBuscar.html", {"cursos": cursos})
    else:
        return render(request, "buscarCurso.html", {"mensaje": "Por favor ingresa una comision"})