from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views


from .views import PollViewSet, ChoiceList, CreateVote, UserCreate


urlpatterns = [
    
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
]
#urlpatterns = [
    #path('register/' , RegisterUser.as_view())
#]

