# Generated by Django 4.0.1 on 2022-01-25 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega1', '0003_alter_libro_titulo_alter_seccion_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='fecha_publicación',
            new_name='fecha_publicacion',
        ),
    ]
