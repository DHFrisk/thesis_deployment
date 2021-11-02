from django.db import models
# from oficinas.models import Oficina
# from users.models import User

# Create your models here.


class Departamento(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=180, null=False, blank=False)
    is_active= models.BooleanField(default=True, null=False, blank=False)
    fk_oficina= models.ForeignKey("oficinas.Oficina", on_delete=models.PROTECT, null=False, blank=False)
    fk_user_creation= models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False, related_name="fk_departamento_user_creation")
    fk_user_edition= models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="fk_departamento_user_edition", null=True,  blank=True)
    date_creation= models.DateTimeField(auto_now_add=True, editable=False)
    date_edition= models.DateTimeField(null=True, blank=True)