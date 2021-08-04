from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_add_departamentogeo", view_add_departamentogeo, name="view_add_departamentogeo"),
    path("view_view_departamentogeo", view_view_departamentogeo, name="view_view_departamentogeo"),
    path("view_change_departamentogeo", view_change_departamentogeo, name="view_change_departamentogeo"),
    path("view_change_single_departamentogeo/<int:id>", view_change_single_departamentogeo, name="view_change_single_departamentogeo"),
    path("view_delete_departamentogeo", view_delete_departamentogeo, name="view_delete_departamentogeo"),
    path("view_delete_departamentogeo", view_delete_departamentogeo, name="view_delete_departamentogeo"),
    path("view_delete_single_departamentogeo/<int:id>", view_delete_single_departamentogeo, name="view_delete_single_departamentogeo"),
    path("view_delete_departamentogeo", view_delete_departamentogeo, name="view_delete_departamentogeo"),
    path("view_deactivate_single_departamentogeo/<int:id>", view_deactivate_single_departamentogeo, name="view_deactivate_single_departamentogeo"),
    #BACKEND URLS
    path("backend_add_departamentogeo", backend_add_departamentogeo, name="backend_add_departamentogeo"),
    path("backend_change_single_departamentogeo", backend_change_single_departamentogeo, name="backend_change_single_departamentogeo"),
    path("backend_delete_single_departamentogeo", backend_delete_single_departamentogeo, name="backend_delete_single_departamentogeo"),
    path("backend_deactivate_single_departamentogeo", backend_deactivate_single_departamentogeo, name="backend_deactivate_single_departamentogeo"),
]
