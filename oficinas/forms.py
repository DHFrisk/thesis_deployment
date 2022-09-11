from django import forms
from .models import Oficina
from edificios.models import Edificio
from users.models import User
from datetime import datetime
from custom_libraries.custom_fields import CustomModelChoiceField


class AddOficinaForm(forms.Form):
    name= forms.CharField(label="Nombre de oficina", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    edificio= CustomModelChoiceField(label="Seleccione edificio", widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=Edificio.objects.filter(is_active=True).order_by("name"))
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True))
    def save(self, commit=True):
        try:
            # user= User.objects.get(id=self.cleaned_data["user_creation"])
            user=self.cleaned_data["user_creation"]
            # edificio=Edificio.objects.get(id=self.cleaned_data["edificio"])
            edificio= self.cleaned_data["edificio"]
            Oficina.objects.create(name=self.cleaned_data["name"], fk_edificio=edificio, fk_user_creation=user)
        except Exception as e:
            raise ValueError(e)


class ChangeOficinaForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de oficina", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    edificio= CustomModelChoiceField(label="Seleccione edificio", widget=forms.Select(attrs={"class":"form-control form-select", "required":True}), queryset=Edificio.objects.filter(is_active=True).order_by("name"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            edificio= self.cleaned_data["edificio"]
            oficina= Oficina.objects.get(id=self.cleaned_data["id"])
            oficina.name=self.cleaned_data["name"]
            oficina.fk_edificio= edificio
            oficina.fk_user_edition= user
            oficina.date_edition= datetime.now()
            oficina.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateOficinaForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de oficina", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True))
    def save(self, commit=True):
        try:
            user= self.cleaned_data["user_edition"]
            oficina= Oficina.objects.get(id=self.cleaned_data["id"])
            oficina.is_active=False
            oficina.fk_user_edition= user
            oficina.date_edition= datetime.now()
            oficina.save()
        except Exception as e:
            raise ValueError(e)


class DeleteOficinaForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de oficina", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
             oficina=Oficina.objects.get(id=self.cleaned_data["id"])
             oficina.delete()
        except Exception as e:
            raise ValueError(e)
