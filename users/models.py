from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import authenticate
from django.apps import apps
from django.contrib.auth.models import Group
# from django.contrib.auth.models import PermissionsMixin 
# from django.core.mail import send_mail
# from django.contrib.auth.base_user import AbstractBaseUser
# from 
# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name, username, password=None, user_creation=None, is_admin=False, is_staff=False, is_superuser=False):
        if not email or not username or not first_name or not last_name:
            raise ValueError("Todos los campos son necesarios: email, usuario, nombre y apellido")
        new_user= self.model(
            email= self.normalize_email(email),
            username= username,
            first_name= first_name,
            last_name= last_name,
            user_creation= user_creation,
            is_admin= is_admin,
            is_staff= is_staff,
            is_superuser= is_superuser
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, username, first_name, last_name, password, user_creation=None):
        new_user= self.create_user(
            email= self.normalize_email(email),
            username= username,
            password=password,
            first_name= first_name,
            last_name= last_name,
            user_creation= user_creation
        )
        new_user.is_admin= True
        new_user.is_staff= True
        new_user.is_superuser= True
        new_user.save(using=self._db)
        return new_user

    # My own methods
    # def authenticateUser(email, username, password):



class User(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(verbose_name="username", max_length=255, unique=True)
    first_name= models.CharField(verbose_name="first name", max_length=50, editable=True) 
    last_name= models.CharField(verbose_name="last name", max_length=50, editable=True)   
    email= models.EmailField(verbose_name="email", max_length=255, unique=True, editable=True) 
    date_joined= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login= models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    user_creation= models.ForeignKey("self", on_delete=models.PROTECT, null=True)
    
    objects= UserManager()

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= ["username", "first_name", "last_name"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_email(self):
        return self.email

    def get_user_allowed_apps(self):
        apps_configs= apps.get_app_configs()
        permissions= [app.label for app in apps_configs if self.has_perm(app.label)]
        return permissions
    
    def set_group(self, group):
        group=Group.objects.get(name=group)#id=group
        group.user_set.add(self)

    def get_group(self, group=None):
        if group==None:
            return self.groups.all()
        else:
            return self.groups.get(name=group)

