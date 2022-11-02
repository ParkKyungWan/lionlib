"""lionlib URL Configuration

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
from django.urls import path

import lionlib_app.views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', lionlib_app.views.index, name="index"),
    path('login', lionlib_app.views.login, name="login"),
    path('register', lionlib_app.views.register, name="register"),

    path('trend', lionlib_app.views.trend, name="trend"),
    path('my', lionlib_app.views.my, name="my"),
    path('new', lionlib_app.views.new, name="new"),
    
    path('all', lionlib_app.views.all, name="all"),
    path('show', lionlib_app.views.show, name="show"),

    #로그인&회원가입 기능
    path('user_create', lionlib_app.views.user_create, name="user_create" ),
    path('user_login', lionlib_app.views.user_login, name="user_login" ),
    path('logout', lionlib_app.views.logout, name="user_logout" ),

]
