from django import forms
from .models import Edificio


class AddEdificioForm(forms.Form):
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    def save(self, commit=True):
        try:
            Edificio.objects.create(name=self.cleaned_data["name"])
        except Exception as e:
            raise ValueError(e)


class ChangeEdificioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    def save(self, commit=True):
        try:
            edificio=Edificio.objects.get(id=self.cleaned_data["id"])
            edificio.name=self.cleaned_data["name"]
            edificio.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateEdificioForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del edificio", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
            edificio=Edificio.objects.get(id=self.cleaned_data["id"])
            edificio.is_active=False
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