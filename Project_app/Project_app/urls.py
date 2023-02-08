"""Project_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path , include
from user import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.base,name="base"),
    path("registeruser/", views.register,name='registeruser'),
    path("loginuser/", views.loginuser,name='loginuser'),
    path("logoutuser",views.logoutuser,name='logoutuser'),
    path("account/",views.account,name='account'),
    path('produse.html',views.produse,name='produse'),
    path('produs/<str:pk>/',views.produs,name='produs')
]
