from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import authenticate
from django.apps import apps
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.contrib.auth.models import Permission


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
    username= models.CharField(verbose_name="username", max_length=255, unique=True, editable=True)
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

    def _user_has_perm(user, perm, obj):
        for backend in auth.get_backends():
            if not hasattr(backend, 'has_perm'):
                continue
            try:
                if backend.has_perm(user, perm, obj):
                    return True
            except PermissionDenied:
                return False
        return False

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.first_name + " " + self.last_name                                                                               

    def get_groups_perms(self):
        try:
            groups=self.get_groups()
            excluded_django_default_apps=["admin", "contenttypes", "sessions", "messages", "staticfiles", "multimedia"]
            apps_configs= apps.get_app_configs()
            system_apps=[]
            permissions=[]
            for group in groups:
                permission_data=[]
                for perm in group.permissions.all():
                    permission_data.append({
                        "id": perm.id,
                        "name": perm.name.upper(),
                        "codename": perm.codename,
                        "app_label": perm.content_type.app_label,
                        "group": group.name,
                        "url": "view_"+str(perm.codename)
                        #str(perm.content_type.app_label)+
                        })
                permissions.append({
                    "group": group.name.upper(),
                    "permissions": permission_data
                    })
            return permissions
        except Exception as e:
            return e
    
    def set_group(self, group):
        group=Group.objects.get(name=group)#id=group
        group.user_set.add(self)
        self.user_permissions.set(group.permissions.all())

    def remove_group(self, group):
        # group=Group.objects.get(name=group)#id=group
        for perm in group.permissions.all():
            self.user_permissions.remove(perm)
        group.user_set.remove(self)

    def get_groups(self, group=None):
        try:
            if group==None:
                return self.groups.all()
            else:
                return self.groups.get(name=group)
        except Exception as e:
            return e

