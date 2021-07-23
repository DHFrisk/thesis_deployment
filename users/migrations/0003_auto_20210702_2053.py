# Generated by Django 2.1.15 on 2021-07-02 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210702_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_creation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]