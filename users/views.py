from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseNotAllowed, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import Group
# Create your views here.

"""
FRONTEND VIEWS
"""

@login_required()
@require_http_methods(["GET"])
def view_dashboard(request, **kwargs):
	print(request.user.get_user_allowed_apps())
	print("---------------------------")
	print(request.user.get_group())
	# print(request.user.groups.all())
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

"""
END FRONTEND VIEWS
"""


"""
BACKEND VIEWS
"""
@require_http_methods(["POST"])
def backend_register(request, *args, **kwargs):
	try:
		context={}
		form= RegistrationForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get("email")
			username= form.cleaned_data.get("username")
			form.save()
			new_user= User.objects.get(email=email, username=username)
			for i in form.cleaned_data.get("groups"):
				new_user.set_group(i.name)
			
			return redirect("alert", message_type="success", message="Usuario: "+username+" registrado exitosamente.", view="view_register")
		else:
			context["registration_form"]= form
			# return redirect("alert", message_type="warning", message="No se han llenado los campos de forma correcta, intente de nuevo.", view="view_register")
			return render(request, "users/registration.html", context)
	except Exception as e:
		return redirect("alert", message_type="error", message=str(e), view="view_register")


@require_http_methods(["POST"])
def backend_login(request, *args, **kwargs):
	try:
		context={}
		form= LoginForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get("email")
			password= form.cleaned_data.get("password")
			user= authenticate(email=email, password=password)
			print(type(user))
			if user is not None and user.is_active:
				print("login")
				login(request, user)
				return redirect("view_dashboard")
			else:
				return redirect("alert", message_type="warning", message="Datos incorrectos.", view="view_login")
		else:
			return redirect("alert", message_type="error", message="Error en el ingreso de las credenciales.", view="view_login")
	except Exception as e:
		return redirect("alert", message_type="error", message=f"Ha ocurrido un error {e}", view="view_login")
"""
END BACKEND VIEWS
"""