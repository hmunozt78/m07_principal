from django.urls import path 

from . import views

urlpatterns = [
    path('', views.listado_productos, name="listado_productos"),
    path('productos/add', views.add_producto, name="add_producto"),
    path('productos/update/<int:id_producto>/', views.update_producto, name="update_producto"),
    path('productos/delete/<int:id_producto>/', views.delete_producto, name="delete_producto"),
   
]
