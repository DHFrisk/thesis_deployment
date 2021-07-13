from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
   # FRONTEND
   path("view_dashboard", view_dashboard, name="view_dashboard"),
   path("view_register", view_register, name="view_register"),
   path("view_login", view_login, name="view_login"),
   path("view_logout", view_logout, name="view_logout"),
   
   # BACKEND
   path("backend_register", backend_register, name="backend_register"),
   path("backend_login", backend_login, name="backend_login"),

]
