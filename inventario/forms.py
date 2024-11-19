from django.forms import ModelForm
from django import forms

from .models import Producto

class ProductoFormAdd(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'descripcion', 
            'precio', 
            'stock', 
            'fecha_vencimiento', 
            'categoria'
            ]
        
        labels = {
            "descripcion": ("Descripción"),
            "categoria": ("Categoría"),
        }
        
        help_texts = {
            "nombre": ("* El nombre debe contener sólo letras, espacio, -"),
            "precio": ("* El precio debe ser mayor a 0"),
            "stock": ("* El stock debe ser mayor o igual a 0"),
        }
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "descripcion": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": 'form-control', 'min': 1}),
            "stock": forms.NumberInput(attrs={"class": 'form-control', 'min': 0}),
            "fecha_vencimiento": forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
            "categoria": forms.Select(attrs={"class": 'form-control'}),
        }
    


class ProductoFormUpdate(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre', 
            'descripcion', 
            'precio', 
            'stock', 
            'fecha_vencimiento', 
            'categoria'
            ]
        
        labels = {
            "descripcion": ("Descripción"),
            "categoria": ("Categoría"),
        }
         
        widgets = {
            "id": forms.HiddenInput(attrs={"class": 'form-control'}),
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "descripcion": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": 'form-control', 'min': 1}),
            "stock": forms.NumberInput(attrs={"class": 'form-control', 'min': 0}),
            "fecha_vencimiento": forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
            "categoria": forms.Select(attrs={"class": 'form-control'}),
        }