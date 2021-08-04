from django import forms
from .models import DepartamentoGeo


class AddDepartamentoForm(forms.Form):
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    def save(self, commit=True):
        try:
            DepartamentoGeo.objects.create(name=self.cleaned_data["name"])
        except Exception as e:
            raise ValueError(e)


class ChangeDepartamentoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    def save(self, commit=True):
        try:
            departamento=DepartamentoGeo.objects.get(id=self.cleaned_data["id"])
            departamento.name=self.cleaned_data["name"]
            departamento.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateDepartamentoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    def save(self, commit=True):
        try:
            departamento=DepartamentoGeo.objects.get(id=self.cleaned_data["id"])
            departamento.is_active=False
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
