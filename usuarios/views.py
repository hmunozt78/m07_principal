from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth.models import Permission

from django.contrib.auth.models import User
from .models import Perfil


#importación de formularios:
from .forms import PerfilFormUpdate, UserFormUpdate

# VISTA BASADA EN CLASE PARA REGISTRO
class UserRegistroView(CreateView):
    form_class =  UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        usuario = form.instance # obtenemos la istancia de la Clase User
        permiso = Permission.objects.get(codename='can_edit_clubes') # obtener permiso desde la base de datos
        usuario.user_permissions.add(permiso) # le agregamos el permiso al usuario
        usuario.save()

        messages.success(self.request, 'Registro exitoso.')
        return response
    
    

# VISTA BASADA EN CLASE PARA LOGIN
class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    
    def form_valid(self, form):
        
        messages.success(self.request, 'Login exitoso.')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
    
#vista de logout
class UserLogoutView(LogoutView):
    next_page = 'index'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Ha cerrado la sesión exitosamente.')
        return super().dispatch(request, *args, **kwargs)
    
    
    
def update_perfil(request, id_usuario):
    contexto = {}
    try:
        usuario = User.objects.get(id=id_usuario)
        
    except User.DoesNotExist:
        messages.error(request, f"No existe un usuario con id: {id_usuario}")
        return redirect('index')
    
    try:
        perfil = Perfil.objects.get(usuario=usuario)
        
    except Perfil.DoesNotExist:
        perfil = Perfil(usuario=usuario)
        perfil.save()
        
    if request.method == 'GET':
        
        form_perfil = PerfilFormUpdate(instance=perfil)
        form_usuario = UserFormUpdate(instance=usuario)
        
        contexto["form_perfil"] = form_perfil
        contexto["form_usuario"] = form_usuario
        
        contexto["perfil"] = perfil
        contexto["usuario"] = usuario
        return render(request, 'usuarios/update_perfil.html', contexto)
        
        
    if request.method == "POST":
        form_perfil = PerfilFormUpdate(request.POST, instance=perfil)
        form_usuario = UserFormUpdate(request.POST, instance=usuario)
        contexto["form_perfil"] = form_perfil
        contexto["form_usuario"] = form_usuario
        
        #cambiar datos del usuario (DJANGO)
        
        # nombre = request.POST.get("nombre")
        
        # usuario.first_name = nombre
        # usuario.save()
        
        #opcional hacer el update en una línea
        
        # User.objects.update(first_name=nombre)
        if form_perfil.is_valid() and form_usuario.is_valid():
            form_perfil.save()
            form_usuario.save()
            messages.success(request, "Perfil actualizado con éxito.")
            return redirect('index')
            
        else:
            messages.error(request, "Revise los datos ingresados en el formulario y vuelva a intentarlo.")
            return render(request, 'usuarios/update_perfil.html', contexto)