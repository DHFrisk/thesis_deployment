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
def view_add_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.add_departamentogeo"):
        form = AddDepartamentoForm(initial={"user_creation":request.user.id})
        return render(request, "departamentos_geo/view_add_departamentogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar departamentos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.view_departamentogeo"):
        departamentos= DepartamentoGeo.objects.filter(is_active=True)
        return render(request, "departamentos_geo/view_view_departamentogeo.html", {"departamentos":departamentos})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver departamentos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.change_departamentogeo"):
        departamentos= DepartamentoGeo.objects.filter(is_active=True)
        return render(request, "departamentos_geo/view_change_departamentogeo.html", {"departamentos":departamentos})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar departamentos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_departamentogeo(request, id):
    if request.user.has_perm("departamentos_geo.change_departamentogeo"):
        departamento=DepartamentoGeo.objects.get(id=id)
        form= ChangeDepartamentoForm(initial={"id":departamento.id, "name":departamento.name, "user_edition":request.user.id})
        return render(request, "departamentos_geo/view_change_single_departamentogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar departamentos.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.delete_departamentogeo"):
        departamentos=DepartamentoGeo.objects.filter(is_active=True)
        return render(request, "departamentos_geo/view_delete_departamentogeo.html", {"departamentos":departamentos})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar departamentos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_departamentogeo(request, id):
    if request.user.has_perm("departamentos_geo.delete_departamentogeo"):
        departamento=DepartamentoGeo.objects.get(id=id)
        form= DeleteDepartamentoForm(initial={"id":departamento.id, "name":departamento.name})
        return render(request, "departamentos_geo/view_delete_single_departamentogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar departamentos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_departamentogeo(request, id):
    if request.user.has_perm("departamentos_geo.delete_departamentogeo"):
        departamento=DepartamentoGeo.objects.get(id=id)
        form= DeactivateDepartamentoForm(initial={"id":departamento.id, "name":departamento.name, "user_edition":request.user.id})
        return render(request, "departamentos_geo/view_delete_single_departamentogeo.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar departamentos.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.add_departamentogeo"):
        try:
            form= AddDepartamentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Departamento registrado exitosamente.", view="view_add_departamentogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_departamentogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar departamentos.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.change_departamentogeo"):
        try:
            form= ChangeDepartamentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Departamento modificado exitosamente.", view="view_change_departamentogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_departamentogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar departamentos.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.delete_departamentogeo"):
        try:
            form= DeactivateDepartamentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Departamento anulado exitosamente.", view="view_delete_departamentogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_departamentogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular departamentos.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_departamentogeo(request):
    if request.user.has_perm("departamentos_geo.delete_departamentogeo"):
        try:
            form= DeleteDepartamentoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Departamento eliminado exitosamente.", view="view_delete_departamentogeo")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_departamentogeo")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar departamentos.", view="view_dashboard")