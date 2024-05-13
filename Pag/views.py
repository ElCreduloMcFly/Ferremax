from django.shortcuts import render

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
