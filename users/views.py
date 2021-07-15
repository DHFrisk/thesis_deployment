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
# Create your views here.

"""
FRONTEND VIEWS
"""

@login_required()
@require_http_methods(["GET"])
def view_dashboard(request, **kwargs):
	return render(request, "users/dashboard.html")


@login_required()
@require_http_methods(["GET"])
def view_register(request):
	form= RegistrationForm(initial={"user_creation": str(User.objects.get(email=request.user.email, username=request.user.username).id)})
	return render(request, "users/registration.html", {"form": form})


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
def view_register_group(request):
	form= GroupRegistrationForm()
	return render(request, "users/groups_registration.html", {"form": form})

"""
END FRONTEND VIEWS
"""


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_register(request):
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
			return redirect("alert", message_type="success", message="Usuario: "+username+" registrado exitosamente.", view="view_register")
		else:
			errors_raw= str(form.errors.as_data())
			# print(type(errors_raw))
			# print(errors_raw)
			return redirect("alert", message_type="warning", message=f"No se han llenado los campos de forma correcta, intente de nuevo. "+errors_raw, view="view_register")
			# return render(request, "users/registration.html", context)
	except Exception as e:
		return redirect("alert", message_type="error", message=str(e), view="view_register")


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
def backend_register_group(request):
	try:
		form= GroupRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("alert", message_type="success", message="Grupo registrado exitosamente.", view="view_register_group")
		else:
			return redirect("alert", message_type="warning", message=f"Ha ocurrido un error{e}", view="view_register_group")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error{e}", view="view_register_group")

"""
END BACKEND VIEWS
"""