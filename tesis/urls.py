"""tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import urls, views
from .views import alert
from django.conf import settings
from django.conf.urls.static import static
from users.views import dashboard

urlpatterns = [
    path("", views.view_login, ""),
    path('admin/', admin.site.urls),
    path("equipo/", include("equipo.urls")),
    path("departamentos/", include("departamentos.urls")),
    path("departamentos_geo/", include("departamentos_geo.urls")),
    path("municipios_geo/", include("municipios_geo.urls")),
    path("edificios/", include("edificios.urls")),
    path("unidades/", include("unidades.urls")),
    path("multimedia/", include("multimedia.urls")),
    path("oficinas/", include("oficinas.urls")),
    path("users/", include("users.urls")),
    # ALERTS
    path("alert/<str:message_type>/<str:message>/<str:view>", alert, name="alert"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
