from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_add_unidad", view_add_unidad, name="view_add_unidad"),
    path("view_view_unidad", view_view_unidad, name="view_view_unidad"),
    path("view_change_unidad", view_change_unidad, name="view_change_unidad"),
    path("view_change_single_unidad/<int:id>", view_change_single_unidad, name="view_change_single_unidad"),
    path("view_delete_unidad", view_delete_unidad, name="view_delete_unidad"),
    path("view_delete_unidad", view_delete_unidad, name="view_delete_unidad"),
    path("view_delete_single_unidad/<int:id>", view_delete_single_unidad, name="view_delete_single_unidad"),
    path("view_delete_unidad", view_delete_unidad, name="view_delete_unidad"),
    path("view_deactivate_single_unidad/<int:id>", view_deactivate_single_unidad, name="view_deactivate_single_unidad"),
    #BACKEND URLS
    path("backend_add_unidad", backend_add_unidad, name="backend_add_unidad"),
    path("backend_change_single_unidad", backend_change_single_unidad, name="backend_change_single_unidad"),
    path("backend_delete_single_unidad", backend_delete_single_unidad, name="backend_delete_single_unidad"),
    path("backend_deactivate_single_unidad", backend_deactivate_single_unidad, name="backend_deactivate_single_unidad"),
]