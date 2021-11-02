from django import forms
from .models import *
from users.models import User
from datetime import datetime
from unidades.models import Unidad
from custom_libraries.custom_fields import CustomModelChoiceField, CustomUserModelChoiceField


class AddAccountingForm(forms.Form):
    # id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de la cuenta", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user_creation= self.cleaned_data["user_creation"]
            Accounting.objects.create(name=self.cleaned_data["name"], fk_user_creation=user_creation)
        except Exception as e:
            raise ValueError(e)


class ChangeAccountingForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de la cuenta", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user_edition = self.cleaned_data["user_edition"]
            acc= Accounting.objects.get(id=self.cleaned_data["id"])
            acc.name = self.cleaned_data["name"]
            acc.fk_user_edition = user_edition
            acc.date_edition = datetime.now()
            acc.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateAccountingForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre de la cuenta", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user_edition = self.cleaned_data["user_edition"]
            acc= Accounting.objects.get(id=self.cleaned_data["id"])
            acc.is_active=False
            acc.fk_user_edition = user_edition
            acc.date_edition = datetime.now()
            acc.save()
        except Exception as e:
            raise ValueError(e)

##############################################################################################
class AddHeaderForm(forms.Form):
    name= forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    date= forms.DateTimeField(label="Fecha")
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            user_creation= self.cleaned_data["user_creation"]
            Header.objects.create(name=self.cleaned_data["name"], fk_user_creation=user_creation, date=self.cleaned_data["date"])
        except Exception as e:
            raise ValueError(e)
##############################################################################################

class AddEquipoForm(forms.Form):
    name= forms.CharField(label="Nombre del equipo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    code= forms.CharField(label="Código del equipo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    accounting = CustomModelChoiceField(label="Número/Código de cuenta",
    widget=forms.Select(attrs={"required": True, "class": "form-control form-select"}), queryset=Accounting.objects.filter(is_active=True).order_by("name"))
    date= forms.DateTimeField(label="Fecha")
    description= forms.CharField(label="Descripción", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=255)
    brand= forms.CharField(label="Marca", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    model= forms.CharField(label="Modelo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    unidad= CustomModelChoiceField(label="Seleccione unidad de destino", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "required":True}), queryset=Unidad.objects.filter(is_active=True).order_by("name"))
    price= forms.DecimalField(label="Valor monetario del equipo", widget=forms.NumberInput(attrs={"step":0.25, "class":"form-control form-control-border border-width-2", "required":True}))
    quantity= forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={"class":"form-control form-control-border border-width-2", "required":True}))
    asset_code= forms.CharField(label="No. de bien", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2"}), max_length=180)
    assigned_user= CustomUserModelChoiceField(label="Seleccione usuario responsable", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "required":True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    user_creation= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            assigned_user= self.cleaned_data["assigned_user"]
            user_creation= self.cleaned_data["user_creation"]
            unidad= self.cleaned_data["unidad"]
            if self.cleaned_data["asset_code"]:
                Equipo.objects.create(
                name=self.cleaned_data["name"],
                code=self.cleaned_data["code"],
                accounting=self.cleaned_data["accounting"], description=self.cleaned_data["description"],
                brand=self.cleaned_data["brand"],
                model=self.cleaned_data["model"],
                fk_unidad=unidad,
                fk_assigned_user=assigned_user,
                fk_user_creation=user_creation,
                order=self.cleaned_data["orden"],
                price=self.cleaned_data["price"],
                asset_code=self.cleaned_data["asset_code"],
                date=self.cleaned_data["date"],
                quantity=self.cleaned_data["quantity"])
            else:
                Equipo.objects.create(name=self.cleaned_data["name"], code=self.cleaned_data["code"], accounting=self.cleaned_data["accounting"], description=self.cleaned_data["description"], brand=self.cleaned_data["brand"], model=self.cleaned_data["model"], fk_unidad=unidad, fk_assigned_user=assigned_user, fk_user_creation=user_creation, order=self.cleaned_data["orden"], price=self.cleaned_data["price"], date=self.cleaned_data["date"], quantity=self.cleaned_data["quantity"])
        except Exception as e:
            raise ValueError(e)


class ChangeEquipoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del equipo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    code= forms.CharField(label="Código del equipo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    header = CustomModelChoiceField(label="Encabezado/Orden", widget=forms.Select(attrs={"readonly": True, "class": "form-control form-select"}), queryset=Header.objects.filter(is_active=True).order_by("name"))
    accounting = CustomModelChoiceField(label="Número/Código de cuenta", widget=forms.Select(attrs={"required": True, "class": "form-control form-select"}), queryset=Accounting.objects.filter(is_active=True).order_by("name"))
    description= forms.CharField(label="Descripción", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=255)
    brand= forms.CharField(label="Marca", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    model= forms.CharField(label="Modelo", widget=forms.TextInput(attrs={"required":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    unidad= CustomModelChoiceField(label="Seleccione unidad de destino", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "required":True}), queryset=Unidad.objects.filter(is_active=True).order_by("name"))
    price = forms.DecimalField(label="Valor monetario del equipo", widget=forms.NumberInput(attrs={"step": 0.25, "class": "form-control form-control-border border-width-2"}))
    quantity= forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={"class":"form-control form-control-border border-width-2", "required":True}))
    asset_code = forms.CharField(label="No. de bien", widget=forms.TextInput(attrs={"class": "form-control form-control-border border-width-2"}), max_length=180)
    assigned_user= CustomUserModelChoiceField(label="Seleccione usuario responsable", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "required":True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
            assigned_user= self.cleaned_data["assigned_user"]
            user_edition= self.cleaned_data["user_edition"]
            unidad= self.cleaned_data["unidad"]
            equipo= Equipo.objects.get(id=self.cleaned_data["id"])
            equipo.fk_last_assigned_user=equipo.fk_assigned_user
            equipo.fk_last_unidad= equipo.fk_unidad
            equipo.name=self.cleaned_data["name"]
            equipo.code=self.cleaned_data["code"]
            equipo.accounting=self.cleaned_data["accounting"]
            equipo.description=self.cleaned_data["description"]
            equipo.brand=self.cleaned_data["brand"]
            equipo.model=self.cleaned_data["model"]
            equipo.fk_unidad=unidad
            # equipo.price=self.cleaned_data["price"]
            equipo.asset_code=self.cleaned_data["asset_code"]
            equipo.fk_assigned_user=assigned_user
            equipo.fk_user_edition=user_edition
            equipo.date_edition=datetime.now()
            equipo.save()
        except Exception as e:
            raise ValueError(e)


class DeactivateEquipoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del equipo", widget=forms.TextInput(attrs={"readonly": True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    code= forms.CharField(label="Código del equipo", widget=forms.TextInput(attrs={"readonly": True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    # accounting= forms.CharField(label="Número/Código de cuenta", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    accounting = CustomModelChoiceField(label="Número/Código de cuenta", widget=forms.Select(attrs={"readonly": True, "class": "form-control form-select"}), queryset=Accounting.objects.filter(is_active=True).order_by("name"))
    description= forms.CharField(label="Descripción", widget=forms.TextInput(attrs={"readonly": True, "class":"form-control form-control-border border-width-2"}), max_length=255)
    brand= forms.CharField(label="Marca", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    model= forms.CharField(label="Modelo", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    unidad= CustomModelChoiceField(label="Seleccione unidad de destino", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "readonly":True}), queryset=Unidad.objects.filter(is_active=True).order_by("name"))
    assigned_user= CustomUserModelChoiceField(label="Usuario responsable", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "readonly":True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
           user_edition= self.cleaned_data["user_edition"]
           equipo= Equipo.objects.get(id=self.cleaned_data["id"])
           equipo.is_active=False
           equipo.fk_user_edition=user_edition
           equipo.date_edition=datetime.now()
           equipo.save()
        except Exception as e:
            raise ValueError(e)


class DeleteEquipoForm(forms.Form):
    id= forms.CharField(label="ID", widget=forms.TextInput(attrs={"class":"form-control form-control-border border-width-2", "readonly": True}))
    name= forms.CharField(label="Nombre del equipo", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    code= forms.CharField(label="Código del equipo", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    accounting= forms.CharField(label="Número/Código de cuenta", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    description= forms.CharField(label="Descripción", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=255)
    brand= forms.CharField(label="Marca", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    model= forms.CharField(label="Modelo", widget=forms.TextInput(attrs={"readonly":True, "class":"form-control form-control-border border-width-2"}), max_length=180)
    unidad= CustomModelChoiceField(label="Seleccione unidad de destino", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "readonly":True}), queryset=Unidad.objects.filter(is_active=True).order_by("name"))
    assigned_user= CustomUserModelChoiceField(label="Seleccione usuario responsable", widget=forms.Select(attrs={"class": "form-control form-select", "data-live-search":"true", "readonly":True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    user_edition= forms.ModelChoiceField(label="", widget=forms.Select(attrs={"hidden": True}), queryset=User.objects.filter(is_active=True).order_by("username"))
    def save(self, commit=True):
        try:
             equipo= Equipo.objects.get(id=self.cleaned_data["id"])
             equipo.delete()
        except Exception as e:
            raise ValueError(e)
