from django.urls import path
from . import views

urlpatterns = [
    path('matricular/<int:estudiante_id>/', views.matricular, name='matricular'),
    path('cursos', views.cursos, name='lista_cursos'),
    path('curso/detalle/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiante/detalle/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
]