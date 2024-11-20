from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(null=True, blank=True)
    celular = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
    class Meta:
        managed = True
        db_table = 'perfiles'