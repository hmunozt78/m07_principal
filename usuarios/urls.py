from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.UserRegistroView.as_view(), name='registro'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('perfil/<int:id_usuario>/', views.update_perfil, name='perfil'),
]