from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
# Create your views here.

"""
FRONTEND VIEWS
"""
@login_required()
@require_http_methods(["GET"])
def view_add_municipiogeo(request):
    if request.user.has_perm("municipios_geo.add_municipiogeo"):
        form = AddMunicipioForm(initial={"user_creation":request.user.id})
        return render(request, "municipios_geo/view_add_municipiogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar municipios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_municipiogeo(request):
    if request.user.has_perm("municipios_geo.view_municipiogeo"):
        municipios= MunicipioGeo.objects.filter(is_active=True)
        return render(request, "municipios_geo/view_view_municipiogeo.html", {"municipios":municipios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver municipios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_municipiogeo(request):
    if request.user.has_perm("municipios_geo.change_municipiogeo"):
        municipios= MunicipioGeo.objects.filter(is_active=True)
        return render(request, "municipios_geo/view_change_municipiogeo.html", {"municipios":municipios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar municipios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_municipiogeo(request, id):
    if request.user.has_perm("municipios_geo.change_municipiogeo"):
        municipio=MunicipioGeo.objects.get(id=id)
        departamento= DepartamentoGeo.objects.get(id=municipio.fk_departamentogeo.id)
        form= ChangeMunicipioForm(initial={"id":municipio.id, "name":municipio.name, "departamentogeo":departamento.id, "user_edition":request.user.id})
        return render(request, "municipios_geo/view_change_single_municipiogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar municipios.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_municipiogeo(request):
    if request.user.has_perm("municipios_geo.delete_municipiogeo"):
        municipios=MunicipioGeo.objects.filter(is_active=True)
        return render(request, "municipios_geo/view_delete_municipiogeo.html", {"municipios":municipios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar municipios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_municipiogeo(request, id):
    if request.user.has_perm("municipios_geo.delete_municipiogeo"):
        municipio=MunicipioGeo.objects.get(id=id)
        form= DeleteMunicipioForm(initial={"id":municipio.id, "name":municipio.name})
        return render(request, "municipios_geo/view_delete_single_municipiogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar municipios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_municipiogeo(request, id):
    if request.user.has_perm("municipios_geo.delete_municipiogeo"):
        municipio=MunicipioGeo.objects.get(id=id)
        form= DeactivateMunicipioForm(initial={"id":municipio.id, "name":municipio.name, "user_edition":request.user.id})
        return render(request, "municipios_geo/view_delete_single_municipiogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar municipios.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_municipiogeo(request):
    if request.user.has_perm("municipios_geo.add_municipiogeo"):
        try:
            form= AddMunicipioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Municipio registrado exitosamente.", view="view_add_municipiogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_municipiogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar municipios.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_municipiogeo(request):
    if request.user.has_perm("municipios_geo.change_municipiogeo"):
        try:
            form= ChangeMunicipioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Municipio modificado exitosamente.", view="view_change_municipiogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_municipiogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar municipios.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_municipiogeo(request):
    if request.user.has_perm("municipios_geo.delete_municipiogeo"):
        try:
            form= DeactivateMunicipioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Municipio anulado exitosamente.", view="view_delete_municipiogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_municipiogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular municipios.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_municipiogeo(request):
    if request.user.has_perm("municipios_geo.delete_municipiogeo"):
        try:
            form= DeleteMunicipioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Municipio eliminado exitosamente.", view="view_delete_municipiogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_municipiogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar municipios.", view="view_dashboard")
