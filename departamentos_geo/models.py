from django.db import models

# Create your models here.


class DepartamentoGeo(models.Model):
    id= models.AutoField(primary_key=True)
    departamento= models.CharField(max_length=180, null=False, blank=False)