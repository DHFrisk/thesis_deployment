from django import forms
from .models import Edificio
from users.models import User
from datetime import datetime


class AddEdificioForm(forms.Form):
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= User.objects.get(id=self.cleaned_data["user_creation"])
            user= self.cleaned_data["user_creation"]
            Edificio.objects.create(name=self.cleaned_data["name"], fk_user_creation=user)
        except Exception as e:
            raise ValueError(e)


class ChangeEdificioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= self.cleaned_data["user_edition"]
            user= self.cleaned_data["user_edition"]
            edificio=Edificio.objects.get(id=self.cleaned_data["id"])
            edificio.name=self.cleaned_data["name"]
            edificio.fk_user_edition= user
            edificio.date_edition= datetime.now()
            edificio.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateEdificioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= self.cleaned_data["user_edition"]
            user= self.cleaned_data["user_edition"]
            edificio=Edificio.objects.get(id=self.cleaned_data["id"])
            edificio.is_active=False
            edificio.fk_user_edition= user
            edificio.date_edition= datetime.now()
            edificio.save()
        except Exception as e:
            raise ValueError(e)


class DeleteEdificioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
             edificio=Edificio.objects.get(id=self.cleaned_data["id"])
             edificio.delete()
        except Exception as e:
            raise ValueError(e)