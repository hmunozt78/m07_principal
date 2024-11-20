from django.contrib import admin

from  .models import Curso, Estudiante
# Register your models here.

#@admin.register(EstudianteAdmin)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", )
    search_fields = ("nombre", "apellido", )
    list_filter = ("cursos", )

#@admin.register(CursoAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", )
    search_fields = ("nombre", "descripcion", )
    list_filter = ("nombre", )
    

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)