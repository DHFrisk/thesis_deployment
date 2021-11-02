from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_view_file", view_view_file, name="view_view_file"),
    path("view_add_file", view_add_file, name="view_add_file"),
    path("view_change_file", view_change_file, name="view_change_file"),
    path("view_change_single_file/<int:id>", view_change_single_file, name="view_change_single_file"),
    path("view_delete_single_file/<int:id>", view_delete_single_file, name="view_delete_single_file"),
    path("view_delete_file", view_delete_file, name="view_delete_file"),

    #BACKEND URLS
    path("backend_add_file", backend_add_file, name="backend_add_file"),
    path("backend_change_single_file", backend_change_single_file, name="backend_change_single_file"),
    path("backend_change_single_file_groups", backend_change_single_file_groups, name="backend_change_single_file_groups"),
    path("backend_delete_single_file", backend_delete_single_file, name="backend_delete_single_file"),

]
