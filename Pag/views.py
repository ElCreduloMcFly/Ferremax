from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import producto,categoria
import json

# Create your views here.
def mostrarhome(request):
    return render(request,'MenuPrincipal.html')

def mostrarherramientas(request):
    return render(request,'herramientas.html')

def mostrarinicio(request):
    return render(request,'InicioSeccion_Registro.html')

def mostrarolvido(request):
    return render(request,'olvidocontraseña.html')

def mostrarcarrito(request):
    return render(request,'carrito.html')

def mostrarvendedor(request):
    return render(request,'inventarioAct.html')

@csrf_exempt
def agregar_producto(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        categoria = categoria.objects.get(id=data['categoria'])
        producto = producto(
            nombre_prod=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['cantidad'],
            id_categoria=categoria
        )
        producto.save()
        return JsonResponse({'message': 'Producto agregado correctamente'}, status=201)

@csrf_exempt
def modificar_producto(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            producto = producto.objects.get(id_prod=id)
            producto.nombre_prod = data['nombre']
            producto.descripcion = data['descripcion']
            producto.precio = data['precio']
            producto.stock = data['cantidad']
            producto.id_categoria = categoria.objects.get(id=data['categoria'])
            producto.save()
            return JsonResponse({'message': 'Producto actualizado correctamente'}, status=200)
        except producto.DoesNotExist:
            return JsonResponse({'message': 'Producto no encontrado'}, status=404)

@csrf_exempt
def borrar_producto(request, id):
    if request.method == 'DELETE':
        try:
            producto = producto.objects.get(id_prod=id)
            producto.delete()
            return JsonResponse({'message': 'Producto eliminado correctamente'}, status=200)
        except producto.DoesNotExist:
            return JsonResponse({'message': 'Producto no encontrado'}, status=404)
