# Generated by Django 4.2.2 on 2024-05-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pag', '0002_rename_teléfono_proveedor_telefono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contrasena_usu',
            field=models.CharField(default='Gd01062018.', max_length=100),
        ),
    ]
