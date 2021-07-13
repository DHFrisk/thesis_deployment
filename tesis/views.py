from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseNotAllowed, HttpResponse
from django.contrib import messages


def alert(request, message_type, message, view):
	if message_type == "info":
		messages.info(request, message)
		return redirect(view)
	if message_type == "success":
		messages.success(request, message)
		return redirect(view)
	if message_type == "warning":
		messages.warning(request, message)
		return redirect(view)
	if message_type == "error":
		messages.error(request, message)
		return redirect(view)
	else:
		messages.error(request, "Ha ocurrido un error")
		return redirect(view)