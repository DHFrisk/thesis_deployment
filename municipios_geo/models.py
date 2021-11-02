from django.db import models
# from departamentos_geo.models import DepartamentoGeo
# Create your models here.


class MunicipioGeo(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=180, null=False, blank=False)
    is_active= models.BooleanField(default=True, null=False, blank=False)
    fk_departamentogeo= models.ForeignKey("departamentos_geo.DepartamentoGeo", on_delete=models.PROTECT, null=False, blank=False)
    fk_user_creation= models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False, related_name="fk_municipiogeo_user_creation")
    fk_user_edition= models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True, related_name="fk_municipiogeo_user_edition")
    date_creation= models.DateTimeField(auto_now_add=True, editable=False)
    date_edition= models.DateTimeField(null=True, blank=True)
