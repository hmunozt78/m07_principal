from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import redirect

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
    
    return render(request, "academia/matricular.html", contexto)
