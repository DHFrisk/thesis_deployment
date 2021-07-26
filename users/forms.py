from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.apps import apps
from functools import partial
from itertools import groupby
from operator import attrgetter
from django.forms.models import ModelChoiceIterator, ModelChoiceField
from django.contrib.auth.password_validation import validate_password


class RegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length=255, help_text="Es necesario una dirección de correo electrónico válida.", label="Dirección de correo electrónico", widget=forms.EmailInput(attrs={"class":"form-control form-control-border border-width-2"}))
    groups= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all(), blank=True)
    # groups= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.SelectMultiple(attrs={"class":"custom-select col-md-12"}), queryset=Group.objects.all(), blank=True)
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}), label="Contraseña (Auto-generada)")
    password2= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}), label="Confirmar contraseña (Auto-generada)")
    class Meta:
        model= User
        fields= ["email", "username", "first_name", "last_name", "password1", "password2", "is_admin", "is_staff", "is_superuser", "user_creation"]
        labels= {
        "email": _("Dirección de correo electrónico"), 
        "username": _("Nombre de usuario"), 
        "first_name": _("Nombre(s)"), 
        "last_name": _("Apellido(s)"), 
        "password1": _("Contraseña (Auto-generada)"), 
        "password2": _("Confirmar contraseña (Auto-generada)"), 
        "is_staff": _("Funcionario"),
        "is_admin": _("Administrador"),
        "is_superuser": _("Super usuario"), 
        "user_creation": _("Usuario de creación")
        }
        widgets= {
        "user_creation": forms.Select(attrs={"hidden": True}),
        "username": forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}),
        "first_name": forms.TextInput(attrs={"class":"form-control form-control-border border-width-2"}),
        "last_name": forms.TextInput(attrs={"class":"form-control form-control-border border-width-2"}),
        }
    
    def save(self, commit=True):
        if self.cleaned_data["password1"] == self.cleaned_data["password2"]:
            if self.cleaned_data["password1"] != None:
                try:
                    new_user= User.objects.create(email=self.cleaned_data["email"], username=self.cleaned_data["username"], first_name=self.cleaned_data["first_name"], last_name=self.cleaned_data["last_name"], is_staff=self.cleaned_data["is_staff"], is_admin=self.cleaned_data["is_admin"], is_superuser=self.cleaned_data["is_superuser"], user_creation=self.cleaned_data["user_creation"])
                    new_user.set_password(self.cleaned_data["password1"])
                    new_user.save()
                except Exception as e:
                    raise ValueError(e)
        else:
            raise ValueError("Las contraseñas generadas no coinciden.")

        
        


class LoginForm(forms.Form):
    email= forms.EmailField(label="Dirección de correo electrónico", widget=forms.EmailInput)
    password= forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class GroupRegistrationForm(forms.Form):
    name= forms.CharField(label="Nombre del grupo", max_length=50, widget=forms.TextInput(attrs={"required":True,"class":"form-control form-control-border border-width-2"}))
    excluded_django_default_apps=["admin", "auth", "contenttypes", "sessions", "messages", "staticfiles"]
    apps_configs= apps.get_app_configs()
    system_apps=[]
    for app in apps_configs:
        if app.label not in excluded_django_default_apps:
            system_apps.append(app.label)
    # permissions=[Permission.objects.filter(content_type__app_label=perm) for perm in system_apps
    choices=[]
    for app in system_apps:
        perm=Permission.objects.filter(content_type__app_label=app).values("id", "content_type_id", "codename", "name")
        if perm:
            nested_tuple=[]
            for choice in perm:
                nested_tuple.append([choice["id"], choice["name"]])
            choices.append((app.upper(), nested_tuple))
    apps_permissions= forms.MultipleChoiceField(label="Permiso(s)", widget=forms.CheckboxSelectMultiple(attrs={"class":"", "style":""}), choices=choices)
    
    def save(self):
        try:
            data=self.cleaned_data
            Group.objects.create(name=data["name"])
        except Exception as e:
            return e


# This form is to update a user profile from an admin profile
class UpdateFormAdmin(forms.Form):
    email= forms.EmailField(max_length=255, help_text="Es necesario una dirección de correo electrónico válida.", label="Dirección de correo electrónico", widget=forms.EmailInput(attrs={"required":True, "class": "form-control form-control-border border-width-2"}))
    username= forms.CharField(label="Nombre de usuario", max_length=255, widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}))
    first_name= forms.CharField(label="Nombre(s)", max_length=255, widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2"}))
    last_name= forms.CharField(label="Apellido(s)", max_length=255, widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2"}))
    is_staff= forms.BooleanField(label="Es staff")
    is_admin= forms.BooleanField(label="Es admin")
    is_superuser= forms.BooleanField(label="Es super-usuario")
    # groups= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.CheckboxSelectMultiple(attrs={"class":""}), queryset="")

    def __init__(self, user, *args, **kwargs):
        super(UpdateFormAdmin, self).__init__(*args, **kwargs)
        self.fields["email"].initial= user.get_email()
        self.fields["username"].initial= user.username
        self.fields["first_name"].initial= user.first_name
        self.fields["last_name"].initial= user.last_name
        self.fields["is_staff"].initial= user.is_staff
        self.fields["is_admin"].initial= user.is_admin
        self.fields["is_superuser"].initial= user.is_superuser
        # self.fields["groups"].queryset= user.groups.all()
        # self.fields["groups"]= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.CheckboxSelectMultiple(attrs={"class":""}), queryset=user.groups.all())


# This form is to update a user profile from an admin profile
class UpdateForm(forms.Form):
    email= forms.EmailField(max_length=255, help_text="Es necesario una dirección de correo electrónico válida.", label="Dirección de correo electrónico")
    groups= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all(), blank=True)
    class Meta:
        model= User
        fields= ["email", "username", "first_name", "last_name", "is_admin", "is_staff", "is_superuser"]
        labels= {
        "email": _("Dirección de correo electrónico"), 
        "username": _("Nombre de usuario"), 
        "first_name": _("Nombre(s)"), 
        "last_name": _("Apellido(s)"), 
        "is_admin": _("Administrador"), 
        "is_staff": _("Funcionario"), 
        "is_superuser": _("Super usuario")
        }
    
    def save(self):
        username= self.cleaned_data["username"]
        email= self.cleaned_data["email"]
        first_name= self.cleaned_data["first_name"]
        last_name= self.cleaned_data["last_name"]
        is_admin= self.cleaned_data["is_admin"]
        is_active= self.cleaned_data["is_active"]
        is_superuser= self.cleaned_data["is_superuser"]
        is_staff= self.cleaned_data["is_staff"]

