from django.urls import path
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_add_departamento", view_add_departamento, name="view_add_departamento"),
    path("view_view_departamento", view_view_departamento, name="view_view_departamento"),
    path("view_change_departamento", view_change_departamento, name="view_change_departamento"),
    path("view_change_single_departamento/<int:id>", view_change_single_departamento, name="view_change_single_departamento"),
    path("view_delete_departamento", view_delete_departamento, name="view_delete_departamento"),
    path("view_delete_departamento", view_delete_departamento, name="view_delete_departamento"),
    path("view_delete_single_departamento/<int:id>", view_delete_single_departamento, name="view_delete_single_departamento"),
    path("view_delete_departamento", view_delete_departamento, name="view_delete_departamento"),
    path("view_deactivate_single_departamento/<int:id>", view_deactivate_single_departamento, name="view_deactivate_single_departamento"),
    #BACKEND URLS
    path("backend_add_departamento", backend_add_departamento, name="backend_add_departamento"),
    path("backend_change_single_departamento", backend_change_single_departamento, name="backend_change_single_departamento"),
    path("backend_delete_single_departamento", backend_delete_single_departamento, name="backend_delete_single_departamento"),
    path("backend_deactivate_single_departamento", backend_deactivate_single_departamento, name="backend_deactivate_single_departamento"),
]
