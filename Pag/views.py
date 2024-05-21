from django.shortcuts import render
from .models import pregunta

# Create your views here.
def mostrarhome(request):
    return render(request,'MenuPrincipal.html')

def mostrarherramientas(request):
    return render(request,'herramientas.html')

def mostrarinicio(request):
    preguntas = pregunta.objects.all()
    
    # Pasar los datos al template
    return render(request, 'InicioSeccion_Registro.html', {'preguntas': preguntas})

def mostrarolvido(request):
    return render(request,'olvidocontraseña.html')

def mostrarcarrito(request):
    return render(request,'carrito.html')

def mostrarvendedor(request):
    return render(request,'inventarioAct.html')
