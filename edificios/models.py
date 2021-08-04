from django.db import models

# Create your models here.

class Edificio(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=180, null=False, blank=False)
    is_active= models.BooleanField(default=True, null=False, blank=False)