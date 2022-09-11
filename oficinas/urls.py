from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_add_oficina", view_add_oficina, name="view_add_oficina"),
    path("view_view_oficina", view_view_oficina, name="view_view_oficina"),
    path("view_change_oficina", view_change_oficina, name="view_change_oficina"),
    path("view_change_single_oficina/<int:id>", view_change_single_oficina, name="view_change_single_oficina"),
    path("view_delete_oficina", view_delete_oficina, name="view_delete_oficina"),
    path("view_delete_oficina", view_delete_oficina, name="view_delete_oficina"),
    path("view_delete_single_oficina/<int:id>", view_delete_single_oficina, name="view_delete_single_oficina"),
    path("view_delete_oficina", view_delete_oficina, name="view_delete_oficina"),
    path("view_deactivate_single_oficina/<int:id>", view_deactivate_single_oficina, name="view_deactivate_single_oficina"),
    #BACKEND URLS
    path("backend_add_oficina", backend_add_oficina, name="backend_add_oficina"),
    path("backend_change_single_oficina", backend_change_single_oficina, name="backend_change_single_oficina"),
    path("backend_delete_single_oficina", backend_delete_single_oficina, name="backend_delete_single_oficina"),
    path("backend_deactivate_single_oficina", backend_deactivate_single_oficina, name="backend_deactivate_single_oficina"),
]