"""lodge URL Configuration

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
from hotels import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo,name='main'),
    path('register1/',views.regisinfo1,name='register1'),
    path('register/',views.regisinfo,name='register'),
    path('verify/',views.verifycred,name='verify'),
    path('logout/',views.booking,name='logout'),
    path('search/',views.booking,name='search'),
    path('forget/', views.forget,name="forget"),
    path('mail_retrive/',views.mail_retrive,name='mail_retrive')
]
