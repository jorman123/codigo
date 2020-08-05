"""tu_ano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('registro_participantes/', views.registro_participantes, name="registro_participantes"),
    path('contact/', views.contact, name="contact"),
    path('galeria/', views.galeria, name="galeria"),
    path('registro_admin/', views.registro_admin, name="registro_admin"),
    path('registro_events/', views.registro_events, name="registro_events"),
    path('blog/', views.blog, name="blog"),
    path('planificacion_conferencia/', views.planificacion_conferencia, name="planificacion_conferencia"),
    path('admin/', admin.site.urls),
]
