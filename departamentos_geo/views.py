from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Permission
# Create your views here.


@login_required()
@require_http_methods(["GET"])
def view_add_departamentogeo(request):
    form = AddDepartamentoForm()
    return render(request, "view_add_departamentogeo.html", {"form":form})
