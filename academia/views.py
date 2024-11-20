from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.db import connection

from .models import Curso, Estudiante



# Create your views here.

def matricular(request, estudiante_id):
    contexto = {}
    
    try:
        estudiante = Estudiante.objects.get(id=estudiante_id)
        
    except estudiante.DoesNotExist:
        messages.error(request, f"No existe el estudiante con id: {estudiante_id}")
        return redirect('index')
    
    contexto["estudiante"] = estudiante
    
    if request.method == 'POST':
        # print(request.POST.get("cursos"))
        
        cursos_seleccionados_template = request.POST.getlist("cursos")
        
        cursos_inscritos = estudiante.cursos.values_list("id", flat=True)
        
        
        # print("cursos seleccionados", cursos_seleccionados)
        #print("cursos inscritos", cursos_inscritos) #<QuerySet [2, 3, 1]>
        
        # ASIGNA AL ESTUDIANTES LOS CURSOS SELECCIONADOS (CHECKED QUE NO TIENE)
        for curso_id in cursos_seleccionados_template:
            if int(curso_id) not in cursos_inscritos:
                curso = Curso.objects.get(id=curso_id)
                estudiante.cursos.add(curso)
        
        for curso_id in cursos_inscritos:
            if str(curso_id) not in cursos_seleccionados_template:
                curso = Curso.objects.get(id=curso_id)
                estudiante.cursos.remove(curso)
                
        estudiante.save()
        
        return redirect("matricular", estudiante_id=estudiante_id)
                
    else:
        
        cursos_disponibles = Curso.objects.exclude(id__in=estudiante.cursos.values_list('id', flat=True))
        
        contexto["cursos_disponibles"] = cursos_disponibles
        contexto["cursos_inscritos"] = estudiante.cursos.all()
        
        return render(request, "academia/matricular.html", contexto)
    
def cursos(request):
    contexto = {}
    cursos = Curso.objects.prefetch_related("estudiantes")
    
    with connection.cursor() as cursor:
        cursor.execute("select count(id) from cursos")
        row = cursor.fetchone()
        print(row)
        cantidad_cursos = row[0]
        contexto["cantidad_cursos"] = cantidad_cursos
        
    contexto["cursos"] = cursos
    return render(request, 'academia/cursos.html', contexto)

def detalle_curso(request, curso_id):
    contexto = {}
    try:
        
        curso =  Curso.objects.get(id=curso_id)
    except curso.DoesNotExist:
        messages.error(request, f"No existe el curso con id: {curso_id}")
        return redirect('cursos')
    
    contexto["curso"] = curso
    
    
    return render(request, 'academia/detalle_curso.html', contexto)

def estudiantes(request):
    contexto = {}
    estudiantes = Estudiante.objects.prefetch_related("cursos")
    contexto["estudiantes"] = estudiantes 
    
    return render(request, "academia/estudiantes.html", contexto)


def detalle_estudiante(request, estudiante_id):
    contexto = {}
    estudiante = Estudiante.objects.prefetch_related("cursos").get(id=estudiante_id)
    contexto["estudiante"] = estudiante 
    
    return render(request, "academia/detalle_estudiante.html", contexto)