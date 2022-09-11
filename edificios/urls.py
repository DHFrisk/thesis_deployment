from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_view_edificio", view_view_edificio, name="view_view_edificio"),
    path("view_add_edificio", view_add_edificio, name="view_add_edificio"),
    path("view_change_edificio", view_change_edificio, name="view_change_edificio"),
    path("view_change_single_edificio/<int:id>", view_change_single_edificio, name="view_change_single_edificio"),
    path("view_delete_edificio", view_delete_edificio, name="view_delete_edificio"),
    path("view_delete_edificio", view_delete_edificio, name="view_delete_edificio"),
    path("view_delete_single_edificio/<int:id>", view_delete_single_edificio, name="view_delete_single_edificio"),
    path("view_delete_edificio", view_delete_edificio, name="view_delete_edificio"),
    path("view_deactivate_single_edificio/<int:id>", view_deactivate_single_edificio, name="view_deactivate_single_edificio"),
    #BACKEND URLS
    path("backend_add_edificio", backend_add_edificio, name="backend_add_edificio"),
    path("backend_change_single_edificio", backend_change_single_edificio, name="backend_change_single_edificio"),
    path("backend_delete_single_edificio", backend_delete_single_edificio, name="backend_delete_single_edificio"),
    path("backend_deactivate_single_edificio", backend_deactivate_single_edificio, name="backend_deactivate_single_edificio"),
]
