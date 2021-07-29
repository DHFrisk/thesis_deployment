from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
   # FRONTEND
   path("view_dashboard", view_dashboard, name="view_dashboard"),
   path("view_add_user", view_add_user, name="view_add_user"),
   path("view_view_user", view_view_user, name="view_view_user"),
   path("view_change_user", view_change_user, name="view_change_user"),
   path("view_change_single_user/<int:user_id>", view_change_single_user, name="view_change_single_user"),
   path("view_delete_user", view_delete_user, name="view_delete_user"),
   path("view_delete_single_user/<int:user_id>", view_delete_single_user, name="view_delete_single_user"),
   path("view_login", view_login, name="view_login"),
   path("view_logout", view_logout, name="view_logout"),
   path("view_add_group", view_add_group, name="view_add_group"),
   path("view_view_group", view_view_group, name="view_view_group"),
   path("view_change_group", view_change_group, name="view_change_group"),
   path("view_change_single_group/<int:group_id>", view_change_single_group, name="view_change_single_group"),
   path("view_delete_group", view_delete_group, name="view_delete_group"),
   path("view_delete_single_group/<int:group_id>", view_delete_single_group, name="view_delete_single_group"),
   
   # path("view_update", view_update, name="view_update"),
   
   # BACKEND
   path("backend_add_user", backend_add_user, name="backend_add_user"),
   path("backend_change_single_user", backend_change_single_user, name="backend_change_single_user"),
   path("backend_change_single_user_groups", backend_change_single_user_groups, name="backend_change_single_user_groups"),
   path("backend_delete_single_user", backend_delete_single_user, name="backend_delete_single_user"),
   path("backend_change_single_group", backend_change_single_group, name="backend_change_single_group"),
   path("backend_change_single_group_permissions", backend_change_single_group_permissions, name="backend_change_single_group_permissions"),
   path("backend_login", backend_login, name="backend_login"),
   path("backend_add_group", backend_add_group, name="backend_add_group"),
   path("backend_delete_single_group", backend_delete_single_group, name="backend_delete_single_group"),

   # path("backend_update", backend_update, name="backend_update"),

]
