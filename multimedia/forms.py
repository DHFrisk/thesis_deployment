from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.apps import apps
from datetime import datetime
from users.models import User

class AddFileForm(forms.Form):
    description= forms.CharField(label="Nombre de archivo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2", "enctype":"multipart/form-data"}), max_length=180)
    groups= forms.ModelMultipleChoiceField(label="Grupo(s) permitido(s)", widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all())
    file = forms.FileField()#label="Archivo", widget=forms. {"required":True, "class":"form-control-file"}
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True))
    def save(self, commit=True):
        try:
            new_file=File.objects.create(fk_user_creation=self.cleaned_data["user_creation"],
                file=self.cleaned_data["file"],
                description=self.cleaned_data["description"])
            for g in self.cleaned_data["groups"]:
                new_file.allowed_groups.add(g)

        except Exception as e:
            raise ValueError(e)


class ChangeFileForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    description= forms.CharField(label="Nombre de archivo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    # groups= forms.ModelMultipleChoiceField(label="Grupo(s) permitido(s)", widget=forms.CheckboxSelectMultiple, queryset=Group.objects.all())
    # file = forms.FileField()
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True))
    def save(self, commit=True):
        try:
            file= File.objects.get(id=self.cleaned_data["id"])
            file.fk_user_edition=self.cleaned_data["user_creation"]
            file.description=self.cleaned_data["description"]
            file.date_edition=datetime.now()

        except Exception as e:
            raise ValueError(e)


class DeleteFileForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    description= forms.CharField(label="Nombre de archivo", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    # file = forms.FileField()
    def save(self, commit=True):
        try:
             file=File.objects.get(id=self.cleaned_data["id"])
             file.delete()
        except Exception as e:
            raise ValueError(e)
