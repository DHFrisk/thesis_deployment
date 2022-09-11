from django.db import models
# from unidades.models import Unidad
# from users.models import User


# this is buy header
class Header(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=255, null=False, blank=False)
   date= models.DateTimeField(null=False, blank=False)
   is_active = models.BooleanField(default=True, null=False, blank=False)
   is_finished= models.BooleanField(default=False, null=False, blank=False)
   fk_user_creation = models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False,related_name="fk_header_user_creation")
   fk_user_edition = models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True,related_name="fk_header_user_edition")
   date_creation = models.DateTimeField(auto_now_add=True, editable=False)
   date_edition = models.DateTimeField(null=True, blank=True, default=None)
   class Meta:
       default_permissions=()


# this is product category
class Accounting(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=180, null=False, blank=False)
   is_active = models.BooleanField(default=True, null=False, blank=False)
   fk_user_creation = models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False,related_name="fk_accounting_user_creation")
   fk_user_edition = models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True,related_name="fk_accouting_user_edition")
   date_creation = models.DateTimeField(auto_now_add=True, editable=False)
   date_edition = models.DateTimeField(null=True, blank=True, default=None)


# this is buy detail
class Equipo(models.Model):
   id= models.AutoField(primary_key=True)
   code= models.CharField(max_length=180, null=False, blank=False)
   name= models.CharField(max_length=180, null=False, blank=False)
   accounting= models.ForeignKey(Accounting, on_delete=models.PROTECT, null=False, blank=False, related_name="fk_equipo_accounting")
   description=models.CharField(max_length=255, null=False, blank=False)
   brand= models.CharField(max_length=180, null=False, blank=False)
   model= models.CharField(max_length=180, null=False, blank=False)
   price= models.DecimalField(max_digits=9, decimal_places=3, null=False, blank=False, editable=False)
   quantity= models.IntegerField(null=False, blank=False, editable=False)
   fk_header= models.ForeignKey(Header, on_delete=models.PROTECT, null=True, blank=True, related_name="fk_equipo_header")
   date= models.DateTimeField(null=True, blank=True)
   asset_code= models.CharField(max_length=180, null=True, blank=True)
   is_active= models.BooleanField(default=True, null=False, blank=False)
   is_in_storage= models.BooleanField(default=False, null=False, blank=False)
   fk_last_unidad= models.ForeignKey("unidades.Unidad", on_delete=models.PROTECT, null=True, blank=True, related_name="fk_equipo_last_unidad")
   fk_unidad= models.ForeignKey("unidades.Unidad", on_delete=models.PROTECT, null=False, blank=False, related_name="fk_equipo_unidad")
   fk_last_assigned_user= models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True, related_name="fk_equipo_last_assigned_user")
   fk_assigned_user= models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, related_name="fk_equipo_assigned_user")
   fk_user_creation= models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False, related_name="fk_equipo_user_creation")
   fk_user_edition= models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True, related_name="fk_equipo_user_edition")
   date_creation= models.DateTimeField(auto_now_add=True, editable=False)
   date_edition= models.DateTimeField(null=True, blank=True, default=None)
