from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseNotAllowed, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import Group
import random, string
import json
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import datetime
# Create your views here.

"""
FRONTEND VIEWS
"""

@login_required()
@require_http_methods(["GET"])
def view_dashboard(request, **kwargs):
	return render(request, "users/dashboard.html")


@require_http_methods(["GET"])
def view_login(request):
	user= request.user
	if user.is_authenticated:
		return redirect("view_dashboard")
	else:
		form= LoginForm()
		return render(request, "users/login.html", {"form": form})


@login_required()
@require_http_methods(["GET"])
def view_logout(request):
	logout(request)
	return redirect("view_login")


@login_required()
@require_http_methods(["GET"])
def view_add_user(request):
	if request.user.has_perm("add_user"):
		form= RegistrationForm(initial={"user_creation": str(User.objects.get(email=request.user.email, username=request.user.username).id)})
		return render(request, "users/view_add_user.html", {"form": form})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para crear usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_user(request):
	if request.user.has_perm("view_user"):
		users= User.objects.filter(is_active=True).values("id", "first_name", "last_name", "email", "is_staff", "is_admin", "is_superuser")
		return render(request, "users/view_view_user.html", {"users": users})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para visualizar usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_user(request):
	if request.user.has_perm("change_user"):
		users= User.objects.filter(is_active=True).values("id", "first_name", "last_name", "email", "is_staff", "is_admin", "is_superuser", "date_joined", "last_login")
		return render(request, "users/view_change_user.html", {"users": users})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_user(request, user_id):
	if request.user.has_perm("change_user"):
		"""I know, I could did it different, but fuck it."""
		user= User.objects.get(id=user_id)
		user_groups= user.get_groups()
		groups= Group.objects.all()
		groups_n= [g for g in groups if g not in user_groups]
		# form= UpdateFormAdmin(user)

		# unlisted_groups= [unlisted_group for unlisted_group in Group.objects.all() if unlisted_group not in form.base_fields["groups"].choices]
		# form.base_fields["groups"].choices= form.base_fields["groups"].choices + unlisted_groups
		# user_groups= user.get_groups()

		form= UpdateFormAdmin(initial={
			"email": user.get_email(),
			"username": user.username,
			"first_name": user.first_name,
			"last_name": user.last_name,
			"is_staff": user.is_staff,
			"is_admin": user.is_admin,
			"is_superuser": user.is_superuser,
			"user_id": user.id
		})
		# for group in range(len(user_groups)):
		# 	for g in range(len(form.base_fields["groups"].choices)):
		# 		if user_groups[group] ==  form.base_fields["groups"].choices[g]:
		# 			print(type(form.base_fields["groups"].choices[g]))
		return render(request, "users/view_change_single_user.html", {"form": form, "user_groups":user_groups, "groups":groups_n, "user_id": user_id})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_user(request):
	if request.user.has_perm("delete_user"):
		users= User.objects.filter(is_active=True).values("id", "first_name", "last_name", "email", "is_staff", "is_admin", "is_superuser", "date_joined", "last_login")
		return render(request, "users/view_delete_user.html", {"users": users})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_user(request, user_id):
	if request.user.has_perm("delete_user"):
		user= User.objects.get(id=user_id)
		user_groups= user.get_groups()
		groups= Group.objects.all()
		groups_n= [g for g in groups if g not in user_groups]
		form= DeleteForm(initial={
			"email": user.get_email(),
			"username": user.username,
			"first_name": user.first_name,
			"last_name": user.last_name,
			"is_staff": user.is_staff,
			"is_admin": user.is_admin,
			"is_superuser": user.is_superuser,
			"user_id": user.id
		})
		return render(request, "users/view_delete_single_user.html", {"form": form, "user_groups":user_groups, "groups":groups_n, "user_id": user_id})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar usuarios.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_add_group(request):
	if request.user.has_perm("add_user"):
		form= GroupRegistrationForm()
		return render(request, "users/view_add_group.html", {"form": form})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para agregar grupos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_view_group(request):
	if request.user.has_perm("view_user"):
		groups= Group.objects.all()
		return render(request, "users/view_view_group.html", {"groups": groups})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para visualizar grupos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_group(request):
	if request.user.has_perm("change_user"):
		groups= Group.objects.all()
		return render(request, "users/view_change_group.html", {"groups": groups})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar grupos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_change_single_group(request, group_id):
	if request.user.has_perm("change_user"):
		group= Group.objects.get(id=group_id)
		group_perms= group.permissions.all()

		excluded_django_default_apps=["admin", "auth", "contenttypes", "sessions", "messages", "staticfiles"]

		apps_configs= apps.get_app_configs()
		system_apps=[]
		choices=[]
		for app in apps_configs:
			if app.label not in excluded_django_default_apps:
				system_apps.append(app.label)
		for app in system_apps:
			perm=Permission.objects.filter(content_type__app_label=app)
			for p in perm:
				if p not in group_perms:	
					nested_tuple=[]
					nested_tuple.append([p.id, p.name])
					choices.append((app.upper(), nested_tuple))

		return render(request, "users/view_change_single_group.html", {"group":group, "group_permissions": group_perms, "permissions": choices})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar grupos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_group(request):
	if request.user.has_perm("change_user"):
		groups= Group.objects.all()
		return render(request, "users/view_delete_group.html", {"groups": groups})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para modificar grupos.", view="view_dashboard")


@login_required()
@require_http_methods(["GET"])
def view_delete_single_group(request, group_id):
	if request.user.has_perm("delete_user"):
		group= Group.objects.get(id=group_id)
		group_perms= group.permissions.all()

		excluded_django_default_apps=["admin", "auth", "contenttypes", "sessions", "messages", "staticfiles"]

		apps_configs= apps.get_app_configs()
		system_apps=[]
		choices=[]
		for app in apps_configs:
			if app.label not in excluded_django_default_apps:
				system_apps.append(app.label)
		for app in system_apps:
			perm=Permission.objects.filter(content_type__app_label=app)
			for p in perm:
				if p not in group_perms:	
					nested_tuple=[]
					nested_tuple.append([p.id, p.name])
					choices.append((app.upper(), nested_tuple))

		return render(request, "users/view_delete_single_group.html", {"group":group, "group_permissions": group_perms, "permissions": choices})
	else:
		return redirect("alert", message_type="error", message= "No tiene los permisos necesarios para eliminar grupos.", view="view_dashboard")

# @login_required()
# @require_http_methods(["GET"])
# def view_update(request, user_id):

"""
END FRONTEND VIEWS
"""


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_add_user(request):
	try:
		context={}
		post= request.POST.copy()
		password_parts= [string.ascii_letters, string.digits]
		password= "".join([random.choice(password_parts[0]) for i in range(12)]) + "".join([random.choice(password_parts[1]) for i in range(12)]) + "".join(random.choice(password_parts[0]) for i in range(4))
		post["password1"]= password
		post["password2"]= password
		request.POST= post
		form= RegistrationForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get("email")
			username= form.cleaned_data.get("username")
			form.save()
			new_user= User.objects.get(email=email, username=username)
			for i in form.cleaned_data.get("groups"):
				new_user.set_group(i.name)
			full_name= new_user.get_full_name()
			new_user.email_user("Cuenta DIDEDUC-HUEHUE creada", f"Hola {full_name}, su contraseña es: {password}")
			return redirect("alert", message_type="success", message="Usuario: "+username+" registrado exitosamente.", view="view_add_user")
		else:
			errors_raw= str(form.errors.as_data())
			return redirect("alert", message_type="warning", message=f"No se han llenado los campos de forma correcta, intente de nuevo. "+errors_raw, view="view_add_user")
	except Exception as e:
		print(e)
		return redirect("alert", message_type="error", message=str(e), view="view_add_user")


@require_http_methods(["POST"])
def backend_change_single_user(request):
	try:
		post= request.POST.copy()
		post["is_staff"]= True if "is_staff" in request.POST else False
		post["is_admin"]= True if "is_admin" in request.POST else False
		post["is_superuser"]= True if "is_superuser" in request.POST else False
		form= UpdateFormAdmin(post)
		if form.is_valid():
			form.save()
			return redirect("alert", message_type="success", message=f"Se han actualizado los datos exitosamente.", view="view_change_user")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error {e}", view="view_change_user")


@require_http_methods(["POST"])
def backend_delete_single_user(request):
	try:
		form= DeleteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("alert", message_type="success", message=f"Se ha eliminado al usuario exitosamente.", view="view_change_user")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error {e}", view="view_delete_user")


@require_http_methods(["POST"])
def backend_change_single_user_groups(request):
	try:
		post= request.POST.copy()
		user_id=int(post["user_id_groups"])
		post.pop("user_id_groups")
		request.POST= post
		user= User.objects.get(id=user_id)
		user_groups= user.groups.all()
		groups= Group.objects.all()

		for group in groups:
			if str(group.id) not in request.POST:
				if group in user_groups:
					user.remove_group(group)
				else:
					pass
			else:
				if group in user_groups:
					pass
				else:
					user.set_group(group)
		return redirect("alert", message_type="success", message="Se han actualizado los grupos del usuario exitosamente.", view="view_change_user")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error {e}", view="view_change_user")


@require_http_methods(["POST"])
def backend_login(request):
	try:
		context={}
		form= LoginForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get("email")
			password= form.cleaned_data.get("password")
			user= authenticate(email=email, password=password)
			print(user)
			if user is not None and user.is_active:
				login(request, user)
				return redirect("view_dashboard")
			else:
				return redirect("alert", message_type="warning", message="Datos incorrectos.", view="view_login")
		else:
			return redirect("alert", message_type="error", message="Error en el ingreso de las credenciales.", view="view_login")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error {e}", view="view_login")


@require_http_methods(["POST"])
def backend_add_group(request):
	try:
		form= GroupRegistrationForm(request.POST)
		if form.is_valid():
			group_name= form.cleaned_data["name"]
			apps_permissions= form.cleaned_data["apps_permissions"]
			form.save()
			group= Group.objects.get(name=group_name)
			for i in apps_permissions:
				perm= Permission.objects.get(id=i)
				group.permissions.add(perm)
			return redirect("alert", message_type="success", message="Grupo registrado exitosamente.", view="view_add_group")
		else:
			return redirect("alert", message_type="warning", message=f"Ha ocurrido un error: {e}", view="view_add_group")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}", view="view_add_group")


@require_http_methods(["POST"])
def backend_change_single_group(request):
	try:
		id= request.POST["id"]
		name= request.POST["name"]
		group=Group.objects.get(id=id)
		group.name= name
		group.save()
		return redirect("alert", message_type="success", message="Nombre de grupo modificado exitosamente.", view="view_change_group")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}.", view="view_change_group")


@require_http_methods(["POST"])
def backend_change_single_group_permissions(request):
	try:
		perms= Permission.objects.all()
		group= Group.objects.get(id=request.POST["id"])
		group_perms= group.permissions.all()
		for perm in perms:
			if str(perm.id) in request.POST:
				if perm not in group_perms:
					group.permissions.add(perm)
			else:
				if perm in group_perms:
					group.permissions.remove(perm)
		return redirect("alert", message_type="success", message="Se han modificado los permisos del grupo exitosamente.", view="view_change_group")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}.", view="view_change_group")	


@require_http_methods(["POST"])
def backend_delete_single_group(request):
	try:
		id= request.POST["id"]
		group=Group.objects.get(id=id)
		group_perms= group.permissions.all()
		group_users= User.objects.filter(groups__id=group.id)
		for u in group_users:
			for gp in group_perms:
				u.user_permissions.remove(gp)
			group.user_set.remove(u)
		for g in group_perms:
			group.permissions.remove(g)
		group.delete()
		return redirect("alert", message_type="success", message="Grupo eliminado exitosamente.", view="view_change_group")
	except Exception as e:
		print(e)
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error: {e}.", view="view_delete_group")

"""
END BACKEND VIEWS
"""