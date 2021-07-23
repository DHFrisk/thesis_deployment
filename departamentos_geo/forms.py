from django import forms
from .models import DepartamentoGeo


class CreationDepartamento(forms.ModelForm):
    departamento= forms.CharField(label="Nombre del departamento", widget=forms.TextInput, max_length=180)
    class Meta:
        model= DepartamentoGeo
        fields=["departamento"]