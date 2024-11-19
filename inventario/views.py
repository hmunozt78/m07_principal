from django.shortcuts import render
from .models import Producto, Categoria
from django.db.models import Q 
from django.db.models import Count, Sum, Avg, Min, Max
from .forms import ProductoFormAdd, ProductoFormUpdate
from django.shortcuts import redirect

from django.contrib import messages

# Create your views here.

def listado_productos(request):
    
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    fecha_vencimiento_min = request.GET.get('fecha_vencimiento_min')
    fecha_vencimiento_max = request.GET.get('fecha_vencimiento_max')
    
    if not nombre:
        nombre = ""
    
    contexto = {}
    productos = Producto.objects.all().order_by('-id')
    
    if nombre:
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(descripcion__icontains=nombre))
        
    if precio_min: 
        productos = productos.filter(precio__gte=precio_min)
        
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
        
    if fecha_vencimiento_min:
        productos = productos.filter(fecha_vencimiento__gte=fecha_vencimiento_min)
        
    if fecha_vencimiento_max:
        productos = productos.filter(fecha_vencimiento__lte=fecha_vencimiento_max)
        
    # utilizamos min y max (built-in functions de python para evitar realizar más consultas a la BD)
    limite_min= min((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None)
    limite_max= max((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None)
    

    contexto["productos"] = productos
    contexto["categorias"] = Categoria.objects.all().order_by('nombre')
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
    contexto["fecha_vencimiento_min"] = fecha_vencimiento_min
    contexto["fecha_vencimiento_max"] = fecha_vencimiento_max
    contexto["limite_min"] = limite_min
    contexto["limite_max"] = limite_max
    

    return render(request, 'inventario/listado_productos.html', contexto)



def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'inventario/add_producto.html', contexto)
    
    if request.method == 'POST':
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'inventario/add_producto.html', contexto)
        
         

def update_producto(request, id_producto):
    contexto = {}
    try:
        producto = Producto.objects.get(id=id_producto)
        
    except Producto.DoesNotExist:
        messages.error(request, f"No existe un producto con id: {id_producto}")
        return redirect('listado_productos')
        
    
    if request.method == 'GET':
        
        producto.fecha_vencimiento = str(producto.fecha_vencimiento).replace("/", "-")
        print(producto.fecha_vencimiento)
        
        form = ProductoFormUpdate(instance=producto)
        contexto["form"] = form
        
        contexto["producto"] = producto
        return render(request, 'inventario/update_producto.html', contexto)
        
        
    if request.method == "POST":
        form = ProductoFormUpdate(request.POST, instance=producto)
        contexto["form"] = form 
        
        errores = ""
        
        if int(request.POST.get("precio")) < 1 :
            errores = errores + "No puede ingresar precios con valor 0 o menos. | "
            
        if int(request.POST.get("stock")) < 0 :
            errores  = errores + "No puede ingresar stock menor a 0."
        
        if errores:
            messages.error(request, errores)
            return render(request, 'inventario/update_producto.html', contexto)

    
        
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado con éxito.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Revise los datos ingresados en el formulario y vuelva a intentarlo.")
            return render(request, 'inventario/update_producto.html', contexto)
         

def delete_producto(request, id_producto):
    
    try:
        producto = Producto.objects.get(id=id_producto)
        
    except Producto.DoesNotExist:
        messages.error(request, f"No existe un producto con id: {id_producto}")
        return redirect('listado_productos')
    
    producto.delete()
        
    messages.success(request, f"Producto con ID: {id_producto} eliminado con éxito.")
    return redirect('listado_productos')


 