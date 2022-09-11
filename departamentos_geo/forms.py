from django import forms
from .models import DepartamentoGeo
from users.models import User
from datetime import datetime
# from custom_libraries.custom_fields import CustomModelChoiceField


class AddDepartamentoForm(forms.Form):
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= User.objects.get(id=self.cleaned_data["user_creation"])
            user= self.cleaned_data["user_creation"]
            DepartamentoGeo.objects.create(name=self.cleaned_data["name"], fk_user_creation=user)
        except Exception as e:
            raise ValueError(e)


class ChangeDepartamentoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= User.objects.get(id=self.cleaned_data["user_edition"])
            user= self.objects.cleaned_data["user_edition"]
            departamento=DepartamentoGeo.objects.get(id=self.cleaned_data["id"])
            departamento.name=self.cleaned_data["name"]
            departamento.fk_user_edition=user
            departamento.date_edition= datetime.now()
            departamento.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateDepartamentoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            # user= User.objects.get(id=self.cleaned_data["user_edition"])
            user= self.cleaned_data["user_edition"]
            departamento=DepartamentoGeo.objects.get(id=self.cleaned_data["id"])
            departamento.is_active=False
            departamento.fk_user_edition=user
            departamento.date_edition= datetime.now()
            departamento.save()
        except Exception as e:
            raise ValueError(e)


class DeleteDepartamentoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
             departamento=DepartamentoGeo.objects.get(id=self.cleaned_data["id"])
             departamento.delete()
        except Exception as e:
            raise ValueError(e)
