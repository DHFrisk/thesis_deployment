from django.db import models
from django.contrib.auth.models import Group

# # Create your models here.


class File(models.Model):
   id= models.AutoField(primary_key=True)
   description=models.CharField(max_length=255, null=False, blank=False)
   allowed_groups=models.ManyToManyField(Group, null=True, blank=True)
   file=models.FileField(upload_to='files/')
   is_active= models.BooleanField(default=True, null=False, blank=False)
   fk_user_creation= models.ForeignKey("users.User", on_delete=models.PROTECT, null=False, blank=False, editable=False, related_name="fk_file_user_creation")
   fk_user_edition= models.ForeignKey("users.User", on_delete=models.PROTECT, null=True, blank=True, related_name="fk_file_user_edition")
   date_creation= models.DateTimeField(auto_now_add=True, editable=False)
   date_edition= models.DateTimeField(null=True, blank=True, default=None)
