# Generated by Django 3.2.5 on 2021-07-17 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': ['can_add_user', 'can_view_user', 'can_change_user', 'can_delete_user']},
        ),
    ]
