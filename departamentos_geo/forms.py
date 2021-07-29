from django import forms
from .models import DepartamentoGeo


class AddDepartamentoForm(forms.ModelForm):
    departamento= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    
    def save(self, commit=True):
        try:
            DepartamentoGeo.objects.create(name=self.cleaned_data["departamento"])
        except Exception as e:
            raise ValueError(e)

class ChangeDepartamentoForm(forms.ModelForm):
    departamento= forms.CharField(label="Nombre del departamento", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
 
