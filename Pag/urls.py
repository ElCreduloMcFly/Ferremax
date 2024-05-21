from django.contrib import admin
from django.urls import path, include
from .views import mostrarhome,mostrarcarrito,mostrarherramientas,mostrarinicio,mostrarvendedor,agregar_producto,borrar_producto,modificar_producto

urlpatterns = [
    path('',mostrarhome,name="MenuPrincipal"),
    path('Carrito',mostrarcarrito,name="Carrito"),
    path('Herramientas',mostrarherramientas,name="Herramientas"),
    path('Inicio',mostrarinicio,name="Sesion"),
    path('Vendedor',mostrarvendedor,name="Vendedor"),
    path('Agregar/',agregar_producto, name='Agregar'),
    path('Modificar/<int:id>/',modificar_producto , name='Modificar'),
    path('Eliminar/<int:id>/',borrar_producto , name='Eliminar'),    
]