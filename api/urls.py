from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views






urlpatterns = [
    
    
    path("register/",views.registerpage,name="register"),
    path("login/", views.loginpage,name="login"),
]

