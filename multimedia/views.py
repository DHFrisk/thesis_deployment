import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Permission
from django.http import HttpResponse
from django.contrib.auth.models import Group

"""
FRONTEND VIEWS
"""
@login_required()
@require_http_methods(["GET"])
def view_add_file(request):
    if request.user.has_perm("multimedia.add_file"):
        form = AddFileForm(initial={"user_creation":request.user.id})
        return render(request, "multimedia/view_add_file.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar multimedia.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_file(request):
    if request.user.has_perm("multimedia.view_file"):
        user_groups= request.user.get_groups()
        user_files= File.objects.filter(is_active=True, fk_user_creation=request.user)
        shared_files= []
        for group in user_groups:
            files=File.objects.filter(is_active=True, allowed_groups=group)
            for f in files:
                shared_files.append({
                    "id":f.id,
                    "description":f.description,
                    "url":f.file.url,
                    "group":group.name
                })
        return render(request, "multimedia/view_view_file.html", {"user_files":user_files, "shared_files":shared_files})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para ver archivos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_file(request):
    if request.user.has_perm("multimedia.change_file"):
        files= File.objects.filter(is_active=True, fk_user_creation=request.user)
        return render(request, "multimedia/view_change_file.html", {"files":files})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar archivos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_file(request, id):
    if request.user.has_perm("multimedia.change_file"):
        file=File.objects.get(id=id)
        form= ChangeFileForm(initial={"id":file.id, "description":file.description, "file":file.file.url})
        file_groups=file.allowed_groups.all()
        groups=Group.objects.all()
        final_groups=[]
        for i in groups:
            if i not in file_groups:
                final_groups.append(i)
        return render(request, "multimedia/view_change_single_file.html", {"form":form, "file_groups":file_groups, "groups":final_groups, "file_id":file.id})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar archivos.", view="view_dashboard")



@login_required()
@require_http_methods(["GET"])
def view_delete_file(request):
    if request.user.has_perm("multimedia.delete_file"):
        files=File.objects.filter(is_active=True, fk_user_creation=request.user)
        return render(request, "multimedia/view_delete_file.html", {"files":files})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar archivos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_file(request, id):
    if request.user.has_perm("multimedia.delete_file"):
        file=File.objects.get(id=id)
        form= ChangeFileForm(initial={"id":file.id, "description":file.description, "user_edition":request.user.id, "file":file.file.url})
        return render(request, "multimedia/view_delete_single_file.html", {"form":form})
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar archivos.", view="view_dashboard")


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_file(request):
    if request.user.has_perm("multimedia.add_file"):
        try:
            form= AddFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Archivo registrado exitosamente.", view="view_add_file")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_add_file")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar archivo.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_file(request):
    if request.user.has_perm("multimedia.change_file"):
        try:
            form= ChangeFileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Archivo modificado exitosamente.", view="view_change_file")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error en el ingreso de datos, intente de nuevo", view="view_change_file")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar archivos.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_change_single_file_groups(request):
    if request.user.has_perm("multimedia.change_file"):
        try:
            file=File.objects.get(id=request.POST["id"])
            post= request.POST.copy()
            post.pop("id")
            request.POST=post
            file_groups=file.allowed_groups.values_list("id")
            groups= Group.objects.all()
            for group in groups:
                print("IS ENTERING")
                # print(request.POST)
                if str(group.id) in request.POST:
                    if str(group.id) not in file_groups:
                        file.allowed_groups.add(group)
                else:
                    file.allowed_groups.remove(group)
            return redirect("alert", message_type="success", message= "Archivo modificado exitosamente.", view="view_change_file")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar archivos.", view="view_dashboard")


@require_http_methods(["POST"])
def backend_delete_single_file(request):
    if request.user.has_perm("multimedia.delete_file"):
        try:
            form= DeleteFileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alert", message_type="success", message= "Archivo eliminado exitosamente.", view="view_delete_file")
            else:
                return redirect("alert", message_type="warning", message= "Ha ocurrido un error al eliminar de datos, intente de nuevo", view="view_delete_file")
        except Exception as e:
            return redirect("alert", message_type="error", message= f"Ha ocurrido un error: {e}", view="view_dashboard")
    else:
        return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar archivos.", view="view_dashboard")
