from django import forms
from .models import Unidad
from departamentos.models import Departamento
from datetime import datetime
from users.models import User
from custom_libraries.custom_fields import CustomModelChoiceField


class AddUnidadForm(forms.Form):
    name= forms.CharField(label="Nombre de unidad", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    departamento= CustomModelChoiceField(label="Seleccione departamento",  widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=Departamento.objects.filter(is_active=True).order_by("name"))
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_creation"]
            departamento= self.cleaned_data["departamento"]
            Unidad.objects.create(name=self.cleaned_data["name"], fk_departamento=departamento, fk_user_creation=user)
        except Exception as e:
            raise ValueError(e)


class ChangeUnidadForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de unidad", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    departamento= CustomModelChoiceField(label="Seleccione departamento",  widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=Departamento.objects.filter(is_active=True).order_by("name"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            departamento= self.cleaned_data["departamento"]
            unidad=Unidad.objects.get(id=self.cleaned_data["id"])
            unidad.name=self.cleaned_data["name"]
            unidad.fk_departamento= departamento
            unidad.fk_user_edition= user
            unidad.date_edition= datetime.now()
            unidad.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateUnidadForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de unidad", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            unidad= Unidad.objects.get(id=self.cleaned_data["id"])
            unidad.is_active=False
            unidad.fk_user_edition= user
            unidad.date_edition= datetime.now()
            unidad.save()
        except Exception as e:
            raise ValueError(e)


class DeleteUnidadForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de unidad", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
             unidad=Unidad.objects.get(id=self.cleaned_data["id"])
             unidad.delete()
        except Exception as e:
            raise ValueError(e)
