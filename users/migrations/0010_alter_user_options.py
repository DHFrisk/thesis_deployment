# Generated by Django 3.2.5 on 2021-07-17 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': ['add_user', 'view_user', 'change_user', 'delete_user']},
        ),
    ]
