# Generated by Django 3.2.8 on 2021-11-02 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0002_departamento_fk_oficina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=180)),
                ('is_active', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_edition', models.DateTimeField(blank=True, null=True)),
                ('fk_departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.departamento')),
            ],
        ),
    ]
