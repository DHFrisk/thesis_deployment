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
def view_add_unidad(request):
    if request.user.has_perm("unidades.add_unidad"):
        form = AddUnidadForm(initial={"user_creation":request.user.id})
        return render(request, "unidades/view_add_unidad.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar unidades.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_unidad(request):
    if request.user.has_perm("unidades.view_unidad"):
        unidades= Unidad.objects.filter(is_active=True)
        return render(request, "unidades/view_view_unidad.html", {"unidades":unidades})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver unidades.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_unidad(request):
    if request.user.has_perm("unidades.change_unidad"):
        unidades= Unidad.objects.filter(is_active=True)
        return render(request, "unidades/view_change_unidad.html", {"unidades":unidades})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar unidades.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_unidad(request, id):
    if request.user.has_perm("unidades.change_unidad"):
        unidad=Unidad.objects.get(id=id)
        form= ChangeUnidadForm(initial={"id":unidad.id, "name":unidad.name, "user_edition":request.user.id, "departamento":unidad.fk_departamento})
        return render(request, "unidades/view_change_single_unidad.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar unidades.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_unidad(request):
    if request.user.has_perm("unidades.delete_unidad"):
        unidades=Unidad.objects.filter(is_active=True)
        return render(request, "unidades/view_delete_unidad.html", {"unidades":unidades})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar unidades.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_unidad(request, id):
    if request.user.has_perm("unidades.delete_unidad"):
        unidad=Unidad.objects.get(id=id)
        form= DeleteUnidadForm(initial={"id":unidad.id, "name":unidad.name})
        return render(request, "unidades/view_delete_single_unidad.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar unidades.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_unidad(request, id):
    if request.user.has_perm("unidades.delete_unidad"):
        unidad=Unidad.objects.get(id=id)
        form= DeactivateUnidadForm(initial={"id":unidad.id, "name":unidad.name, "user_edition":request.user.id})
        return render(request, "unidades/view_delete_single_unidad.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar unidades.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_unidad(request):
    if request.user.has_perm("unidades.add_unidad"):
        try:
            form= AddUnidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Unidad registrado exitosamente.", view="view_add_unidad")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_unidad")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar unidades.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_unidad(request):
    if request.user.has_perm("unidades.change_unidad"):
        try:
            form= ChangeUnidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Unidad modificado exitosamente.", view="view_change_unidad")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_unidad")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar unidades.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_unidad(request):
    if request.user.has_perm("unidades.delete_unidad"):
        try:
            form= DeactivateUnidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Unidad anulado exitosamente.", view="view_delete_unidad")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_unidad")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular unidades.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_unidad(request):
    if request.user.has_perm("unidades.delete_unidad"):
        try:
            form= DeleteUnidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Unidad eliminado exitosamente.", view="view_delete_unidad")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_unidad")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar unidades.", view="view_dashboard")