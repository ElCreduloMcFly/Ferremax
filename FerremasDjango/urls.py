from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Pag.urls')),
     path('', views.mostrarhome, name='home'),
    path('herramientas/', views.mostrarherramientas, name='herramientas'),
    path('inicio/', views.mostrarinicio, name='inicio'),
    path('olvido/', views.mostrarolvido, name='olvido'),
    path('carrito/', views.mostrarcarrito, name='carrito'),
    path('vendedor/', views.mostrarvendedor, name='vendedor'),
    path('api/productos/', views.agregar_producto, name='agregar_producto'),
    path('api/productos/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('api/productos/<int:id>/', views.borrar_producto, name='borrar_producto'),
]
#pip install djangorestframework


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



