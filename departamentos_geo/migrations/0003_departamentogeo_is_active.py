# Generated by Django 3.2.5 on 2021-08-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos_geo', '0002_rename_departamento_departamentogeo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamentogeo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
