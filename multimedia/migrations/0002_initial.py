# Generated by Django 3.2.8 on 2021-11-02 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('multimedia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='fk_user_creation',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='fk_file_user_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='fk_user_edition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fk_file_user_edition', to=settings.AUTH_USER_MODEL),
        ),
    ]
