# Generated by Django 3.2.5 on 2021-07-17 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': [('can_add_user', 'Agregar usuario'), ('can_view_user', 'Ver usuario'), ('can_change_user', 'Editar usuario'), ('can_delete_user', 'Eliminar usuario')]},
        ),
    ]
