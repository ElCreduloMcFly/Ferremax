from django.contrib import admin
from django.urls import path
from .views import mostrarhome,mostrarcarrito,mostrarherramientas,mostrarinicio,mostrarvendedor

urlpatterns = [
    path('',mostrarhome,name="MenuPrincipal"),
    path('Carrito/',mostrarcarrito,name="Carrito"),
    path('Herramientas/',mostrarherramientas,name="Herramientas"),
    path('Inicio/',mostrarinicio,name="Sesion"),
    path('Vendedor/',mostrarvendedor,name="Vendedor"),
]