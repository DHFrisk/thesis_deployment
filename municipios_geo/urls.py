from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
    #FRONTEND URLS
    path("view_add_municipiogeo", view_add_municipiogeo, name="view_add_municipiogeo"),
    path("view_view_municipiogeo", view_view_municipiogeo, name="view_view_municipiogeo"),
    path("view_change_municipiogeo", view_change_municipiogeo, name="view_change_municipiogeo"),
    path("view_change_single_municipiogeo/<int:id>", view_change_single_municipiogeo, name="view_change_single_municipiogeo"),
    path("view_delete_municipiogeo", view_delete_municipiogeo, name="view_delete_municipiogeo"),
    path("view_delete_municipiogeo", view_delete_municipiogeo, name="view_delete_municipiogeo"),
    path("view_delete_single_municipiogeo/<int:id>", view_delete_single_municipiogeo, name="view_delete_single_municipiogeo"),
    path("view_delete_municipiogeo", view_delete_municipiogeo, name="view_delete_municipiogeo"),
    path("view_deactivate_single_municipiogeo/<int:id>", view_deactivate_single_municipiogeo, name="view_deactivate_single_municipiogeo"),
    #BACKEND URLS
    path("backend_add_municipiogeo", backend_add_municipiogeo, name="backend_add_municipiogeo"),
    path("backend_change_single_municipiogeo", backend_change_single_municipiogeo, name="backend_change_single_municipiogeo"),
    path("backend_delete_single_municipiogeo", backend_delete_single_municipiogeo, name="backend_delete_single_municipiogeo"),
    path("backend_deactivate_single_municipiogeo", backend_deactivate_single_municipiogeo, name="backend_deactivate_single_municipiogeo"),
]