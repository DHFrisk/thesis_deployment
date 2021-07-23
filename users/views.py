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
	form= RegistrationForm(initial={"user_creation": str(User.objects.get(email=request.user.email, username=request.user.username).id)})
	return render(request, "users/view_add_user.html", {"form": form})


@login_required()
@require_http_methods(["GET"])
def view_view_user(request):
	users= User.objects.filter(is_active=True).values("id", "first_name", "last_name", "email", "is_staff", "is_admin", "is_superuser")
	return render(request, "users/view_view_user.html", {"users": users})


@login_required()
@require_http_methods(["GET"])
def view_change_user(request):
	users= User.objects.filter(is_active=True).values("id", "first_name", "last_name", "email", "is_staff", "is_admin", "is_superuser", "date_joined", "last_login")
	return render(request, "users/view_change_user.html", {"users": users})


@login_required()
@require_http_methods(["GET"])
def view_change_single_user(request, user_id):
	"""I know, I could did it different, but fuck it."""
	user= User.objects.get(id=user_id)
	user_groups= user.get_groups()
	groups= Group.objects.all()
	groups_n= [g for g in groups if g not in user_groups]
	form= UpdateFormAdmin(user)

	# unlisted_groups= [unlisted_group for unlisted_group in Group.objects.all() if unlisted_group not in form.base_fields["groups"].choices]
	# form.base_fields["groups"].choices= form.base_fields["groups"].choices + unlisted_groups
	# user_groups= user.get_groups()

	# form= UpdateFormAdmin(initial={
	# 	"email": user.get_email(),
	# 	"username": user.username,
	# 	"first_name": user.first_name,
	# 	"last_name": user.last_name,
	# 	"is_staff": user.is_staff,
	# 	"is_admin": user.is_admin,
	# 	"is_superuser": user.is_superuser,
	# })
	# for group in range(len(user_groups)):
	# 	for g in range(len(form.base_fields["groups"].choices)):
	# 		if user_groups[group] ==  form.base_fields["groups"].choices[g]:
	# 			print(type(form.base_fields["groups"].choices[g]))


	return render(request, "users/view_change_single_user.html", {"form": form, "user_groups":user_groups, "groups":groups_n})



@login_required()
@require_http_methods(["GET"])
def view_add_group(request):
	form= GroupRegistrationForm()
	return render(request, "users/view_add_group.html", {"form": form})


# @login_required()
# @require_http_methods(["GET"])
# def view_update(request, user_id):
# 	user= User.objects.get(id=user_id)
# 	form= UpdateForm()
# 	form["email"]= user.get_email()
# 	form["username"]= user.get_username()
# 	form["is_active"]= user.is_active
# 	form["is_staff"]= user.is_staff
# 	form["is_admin"]= user.is_admin
# 	form["is_superuser"]= user.is_superuser
# 	form["groups"]= user.get
	
# 	return render(request, "users/update.html", {"form": form})
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


# @require_http_methods(["POST"])
# def backend_update(request):
# 	try:
# 		form= UpdateForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			for i in form.cleaned_data.get("groups"):
# 				new_user.set_group(i.name)
# 	except Exception as e:


@require_http_methods(["POST"])
def backend_login(request):
	try:
		context={}
		form= LoginForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get("email")
			password= form.cleaned_data.get("password")
			user= authenticate(email=email, password=password)
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

"""
END BACKEND VIEWS
"""