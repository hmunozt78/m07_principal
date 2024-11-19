from django.shortcuts import render

def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)