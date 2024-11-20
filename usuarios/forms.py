from django.forms import ModelForm
from django import forms

from .models import Perfil
from django.contrib.auth.models import User


class UserFormUpdate(ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name'
        ]
        
        labels = {
            "first_name": ("Nombre"),
            "last_name": ("Apellido"),
        }
         
        widgets = {
            "username": forms.TextInput(attrs={"class": 'form-control'}),
            "first_name": forms.TextInput(attrs={"class": 'form-control'}),
            "last_name": forms.TextInput(attrs={"class": 'form-control'}),
        }

class PerfilFormUpdate(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'biografia', 
            'celular',
        ]
        
        labels = {
            "biografia": ("Biografía"),
        }
        
        widgets = {
            "biografia": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "celular": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 13}),
        }
