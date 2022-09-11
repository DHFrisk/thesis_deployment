from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_view_equipo", view_view_equipo, name="view_view_equipo"),
    path("view_add_equipo", view_add_equipo, name="view_add_equipo"),
    path("view_change_equipo", view_change_equipo, name="view_change_equipo"),
    path("view_change_single_equipo/<int:id>", view_change_single_equipo, name="view_change_single_equipo"),
    path("view_delete_single_equipo/<int:id>", view_delete_single_equipo, name="view_delete_single_equipo"),
    path("view_delete_equipo", view_delete_equipo, name="view_delete_equipo"),
    path("view_deactivate_single_equipo/<int:id>", view_deactivate_single_equipo, name="view_deactivate_single_equipo"),

    path("view_view_accounting", view_view_accounting, name="view_view_accounting"),
    path("view_add_accounting", view_add_accounting, name="view_add_accounting"),
    path("view_change_accounting", view_change_accounting, name="view_change_accounting"),
    path("view_change_single_accounting/<int:id>", view_change_single_accounting, name="view_change_single_accounting"),
    path("view_delete_accounting", view_delete_accounting, name="view_delete_accounting"),
    path("view_deactivate_single_accounting/<int:id>", view_deactivate_single_accounting, name="view_deactivate_single_accounting"),

    path("view_add_incomes_header", view_add_incomes_header, name="view_add_incomes_header"),

    #BACKEND URLS
    path("backend_add_equipo", backend_add_equipo, name="backend_add_equipo"),
    path("backend_change_single_equipo", backend_change_single_equipo, name="backend_change_single_equipo"),
    path("backend_delete_single_equipo", backend_delete_single_equipo, name="backend_delete_single_equipo"),
    path("backend_deactivate_single_equipo", backend_deactivate_single_equipo, name="backend_deactivate_single_equipo"),

    path("backend_add_accounting", backend_add_accounting, name="backend_add_accounting"),
    path("backend_change_single_accounting", backend_change_single_accounting, name="backend_change_single_accounting"),
    path("backend_deactivate_single_accounting", backend_deactivate_single_accounting, name="backend_deactivate_single_accounting"),

    path("backend_add_incomes_header", backend_add_incomes_header, name="backend_add_incomes_header"),

    #REPORTS
    path("write_responsibility_sheet/<int:equipment_id>", write_responsibility_sheet, name="write_responsibility_sheet"),
    path("write_general_report", write_general_report, name="write_general_report"),
]
