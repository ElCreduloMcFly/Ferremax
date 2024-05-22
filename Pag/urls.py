from django.contrib import admin
from django.urls import path
from .views import mostrarhome,mostrarcarrito,mostrarherramientas,mostrarinicio,mostrarvendedor,iniciarsesion,registrar,finsesion,mostraragregar,agregarproducto,eliminarproducto,modificarproducto,mostrarproducto

urlpatterns = [
    path('',mostrarhome,name="MenuPrincipal"),
    path('Carrito/',mostrarcarrito,name="Carrito"),
    path('Herramientas/',mostrarherramientas,name="Herramientas"),
    path('Inicio/',mostrarinicio,name="Sesion"),
    path('Vendedor/',mostrarvendedor,name="Vendedor"),
    path('mostrarproducto/',mostraragregar,name="mostrarcategoria"),
    path('iniciarsesion/', iniciarsesion, name='iniciarsesion'),   
    path('registrar/',registrar,name="registrar"),
    path('finsesion/',finsesion, name='finsesion'),
    path('agregarproducto/',agregarproducto, name='agregarproducto'),
    path('eliminarproducto/<id_prod>',eliminarproducto, name='eliminarproducto'),
    path('mostrarproducto/<int:id_prod>',mostrarproducto, name='mostrarproducto'),
    path('modificarproducto/<int:id_prod>',modificarproducto, name='modificarproducto'),
]