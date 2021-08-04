from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Permission
# Create your views here.

"""
FRONTEND VIEWS
"""
@login_required()
@require_http_methods(["GET"])
def view_add_edificio(request):
    if request.user.has_perm("add_edificio"):
        form = AddEdificioForm()
        return render(request, "edificios/view_add_edificio.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar edificios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_edificio(request):
    if request.user.has_perm("view_edificio"):
        edificios= Edificio.objects.filter(is_active=True)
        return render(request, "edificios/view_view_edificio.html", {"edificios":edificios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver edificios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_edificio(request):
    if request.user.has_perm("change_edificio"):
        edificios= Edificio.objects.filter(is_activeTrue)
        return render(request, "edificios/view_change_edificio.html", {"edificios":edificios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar edificios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_edificio(request, id):
    if request.user.has_perm("change_edificio"):
        edificio=Edificio.objects.get(id=id)
        form= ChangeEdificioForm(initial={"id":edificio.id, "name":edificio.name})
        return render(request, "edificios/view_change_single_edificio.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar edificios.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_edificio(request):
    if request.user.has_perm("delete_edificio"):
        edificios=Edificio.objects.filter(is_active=True)
        return render(request, "edificios/view_delete_edificio.html", {"edificios":edificios})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar edificios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_edificio(request, id):
    if request.user.has_perm("delete_edificio"):
        edificio=Edificio.objects.get(id=id)
        form= DeleteEdificioForm(initial={"id":edificio.id, "name":edificio.name})
        return render(request, "edificios/view_delete_single_edificio.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar edificios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_edificio(request, id):
    if request.user.has_perm("delete_edificio"):
        edificio=Edificio.objects.get(id=id)
        form= DeactivateEdificioForm(initial={"id":edificio.id, "name":edificio.name})
        return render(request, "edificios/view_delete_single_edificio.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar edificios.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_edificio(request):
    if request.user.has_perm("add_edificio"):
        try:
            form= AddEdificioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Edificio registrado exitosamente.", view="view_add_edificio")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_edificio")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar edificios.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_edificio(request):
    if request.user.has_perm("change_edificio"):
        try:
            form= ChangeEdificioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Edificio modificado exitosamente.", view="view_change_edificio")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar edificios.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_edificio(request):
    if request.user.has_perm("delete_edificio"):
        try:
            form= DeactivateEdificioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Edificio anulado exitosamente.", view="view_delete_edificio")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_edificio")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular edificios.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_edificio(request):
    if request.user.has_perm("delete_edificio"):
        try:
            form= DeleteEdificioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Edificio eliminado exitosamente.", view="view_delete_edificio")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_edificio")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar edificios.", view="view_dashboard")