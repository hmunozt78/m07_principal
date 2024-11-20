from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.URLField(blank=False, null=False, default="https://st3.depositphotos.com/16203680/19307/v/950/depositphotos_193076602-stock-illustration-question-mark-hand-drawn-symbol.jpg")   
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'cursos'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    cursos = models.ManyToManyField(Curso, related_name="estudiantes", blank=True)
    
    def __str__(self):
        return  f"{self.nombre} {self.apellido}"
    
    class Meta:
        managed = True
        db_table = 'estudiantes'