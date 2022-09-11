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
def view_add_oficina(request):
    if request.user.has_perm("oficinas.add_oficina"):
        form = AddOficinaForm(initial={"user_creation":request.user.id})
        return render(request, "oficinas/view_add_oficina.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar oficinas.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_oficina(request):
    if request.user.has_perm("oficinas.view_oficina"):
        oficinas= Oficina.objects.filter(is_active=True)
        return render(request, "oficinas/view_view_oficina.html", {"oficinas":oficinas})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver oficinas.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_oficina(request):
    if request.user.has_perm("oficinas.change_oficina"):
        oficinas= Oficina.objects.filter(is_active=True)
        return render(request, "oficinas/view_change_oficina.html", {"oficinas":oficinas})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar oficinas.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_oficina(request, id):
    if request.user.has_perm("oficinas.change_oficina"):
        oficina=Oficina.objects.get(id=id)
        edificio= Edificio.objects.get(id=oficina.fk_edificio.id)
        form= ChangeOficinaForm(initial={"id":oficina.id, "name":oficina.name, "edificio":edificio.id, "user_edition":request.user.id})
        return render(request, "oficinas/view_change_single_oficina.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar oficinas.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_oficina(request):
    if request.user.has_perm("oficinas.delete_oficina"):
        oficinas=Oficina.objects.filter(is_active=True)
        return render(request, "oficinas/view_delete_oficina.html", {"oficinas":oficinas})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar oficinas.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_oficina(request, id):
    if request.user.has_perm("oficinas.delete_oficina"):
        oficina=Oficina.objects.get(id=id)
        form= DeleteOficinaForm(initial={"id":oficina.id, "name":oficina.name})
        return render(request, "oficinas/view_delete_single_oficina.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar oficinas.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_deactivate_single_oficina(request, id):
    if request.user.has_perm("oficinas.delete_oficina"):
        oficina=Oficina.objects.get(id=id)
        form= DeactivateOficinaForm(initial={"id":oficina.id, "name":oficina.name, "user_edition":request.user.id})
        return render(request, "oficinas/view_delete_single_oficina.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar oficinas.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_oficina(request):
    if request.user.has_perm("oficinas.add_oficina"):
        try:
            form= AddOficinaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Oficina registrada exitosamente.", view="view_add_oficina")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_oficina")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar oficinas.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_oficina(request):
    if request.user.has_perm("oficinas.change_oficina"):
        try:
            form= ChangeOficinaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Oficina modificada exitosamente.", view="view_change_oficina")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_oficina")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar oficinas.", view="view_dashboard")



@require_http_methods(["POST"])
def backend_deactivate_single_oficina(request):
    if request.user.has_perm("oficinas.delete_oficina"):
        try:
            form= DeactivateOficinaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Oficina anulada exitosamente.", view="view_delete_oficina")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al anular de datos, intente de nuevo", view="view_delete_oficina")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para anular oficinas.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_oficina(request):
    if request.user.has_perm("oficinas.delete_oficina"):
        try:
            form= DeleteOficinaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Oficina eliminada exitosamente.", view="view_delete_oficina")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_oficina")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar oficinas.", view="view_dashboard")
