# Generated by Django 3.2.5 on 2021-07-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartamentoGeo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=180)),
            ],
        ),
    ]
