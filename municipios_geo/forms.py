from django import forms
from .models import MunicipioGeo
from departamentos_geo.models import DepartamentoGeo
from users.models import User
from datetime import datetime
from custom_libraries.custom_fields import CustomModelChoiceField


class AddMunicipioForm(forms.Form):
    name= forms.CharField(label="Nombre del municipio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    departamentogeo= CustomModelChoiceField(label="Seleccione departamento", widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=DepartamentoGeo.objects.filter(is_active=True).order_by("name"))
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_creation"]
            departamento= self.cleaned_data["departamentogeo"]
            MunicipioGeo.objects.create(name=self.cleaned_data["name"], fk_departamentogeo=departamento, fk_user_creation=user)
        except Exception as e:
            raise ValueError(e)


class ChangeMunicipioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del municipio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    departamentogeo= CustomModelChoiceField(label="Seleccione departamento", widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=DepartamentoGeo.objects.filter(is_active=True).order_by("name"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            departamento= self.cleaned_data["departamentogeo"]
            municipio=MunicipioGeo.objects.get(id=self.cleaned_data["id"])
            municipio.name=self.cleaned_data["name"]
            municipio.fk_departamentogeo= departamento
            municipio.fk_user_edition= user
            municipio.date_edition= datetime.now()
            municipio.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateMunicipioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del municipio", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            muncipio=MunicipioGeo.objects.get(id=self.cleaned_data["id"])
            muncipio.is_active=False
            muncipio.fk_user_edition= user
            muncipio.date_edition= datetime.now()
            muncipio.save()
        except Exception as e:
            raise ValueError(e)


class DeleteMunicipioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del municipio", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
             muncipio=MunicipioGeo.objects.get(id=self.cleaned_data["id"])
             muncipio.delete()
        except Exception as e:
            raise ValueError(e)
