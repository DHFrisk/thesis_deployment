from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


class RegistrationForm(UserCreationForm):
    email= forms.EmailField(max_length=255, help_text="Es necesario una dirección de correo electrónico válida.", label="Dirección de correo electrónico")
    groups= forms.ModelMultipleChoiceField(label="Grupo(s)", widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all(), blank=True)
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"readonly": True}), label="Contraseña (Auto-generada)")
    password2= forms.CharField(widget=forms.PasswordInput(attrs={"readonly": True}), label="Confirmar contraseña (Auto-generada)")
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
        "is_admin": _("Administrador"), 
        "is_staff": _("Funcionario"), 
        "is_superuser": _("Super usuario"), 
        "user_creation": _("Usuario de creación")
        }
        widgets= {
        # "user_creation": forms.TextInput(attrs={"readonly": "readonly"})
        "user_creation": forms.Select(attrs={"hidden": True}),
        "password1": forms.PasswordInput(attrs={"hidden": True}),
        "password2": forms.PasswordInput(attrs={"hidden": True})
        }

    def clean_email(self):
        email= self.cleaned_data["email"].lower()
        try:
            user= User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError("La dirección de correo electrónico ingresada ya está registrada.")

    def clean_username(self):
        username= self.cleaned_data["username"]
        try:
            user= User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError("El nombre de usuario ingresado ya está registrada.")


class LoginForm(forms.Form):
    email= forms.EmailField(label="Dirección de correo electrónico", widget=forms.EmailInput)
    password= forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class GroupRegistrationForm(forms.Form):
    name= forms.CharField(label="Nombre del grupo", widget=forms.TextInput, max_length=50)

    def save(self):
        try:
            data=self.cleaned_data
            Group.objects.create(name=data["name"])
        except Exception as e:
            return e