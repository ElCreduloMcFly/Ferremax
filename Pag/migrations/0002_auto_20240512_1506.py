from django.db import migrations
from Pag.models import rol, pregunta, categoria, proveedor


def insert_initial_data(apps, schema_editor):
    # Insertar roles
    rol.objects.bulk_create([
        rol(nombre_rol='Admin'),
        rol(nombre_rol='Vendedor'),
        rol(nombre_rol='Bodeguero'),
        rol(nombre_rol='Contador'),
        rol(nombre_rol='Usuario'),
    ])

    # Insertar preguntas
    pregunta.objects.bulk_create([
        pregunta(nombre_preg='¿Cuál es tu color favorito?'),
        pregunta(nombre_preg='¿Cuál es el nombre de tu mascota?'),
        pregunta(nombre_preg='¿En qué ciudad naciste?'),
    ])

    # Insertar categorías
    categoria.objects.bulk_create([
        categoria(nombre_categoria='Herramienta'),
        categoria(nombre_categoria='Eléctrico'),
        categoria(nombre_categoria='Hogar'),
        categoria(nombre_categoria='Estructura'),
        categoria(nombre_categoria='Pieza'),
    ])

    # Insertar proveedores
    proveedor.objects.bulk_create([
        proveedor(nombre_prov='Sodimac', direccion_prov='Lachinchulina #4567', correo='Sodimac@gmail.com', telefono=123456789),
        proveedor(nombre_prov='Easy', direccion_prov='Quilicumbia #4991', correo='Easy@gmail.com', telefono=987654321),
        # Agrega más proveedores según sea necesario
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('Pag', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(insert_initial_data),
    ]

