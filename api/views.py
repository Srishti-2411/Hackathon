from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets


class PollViewSet(viewsets.ModelViewSet):
    # ...

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not delete this poll.")
        return super().destroy(request, *args, **kwargs)


class ChoiceList(generics.ListCreateAPIView):
    # ...

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not create choice for this poll.")
        return super().post(request, *args, **kwargs)

class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer    

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer  



# Create your views here.
#class RegisterUser(APIView):
    #def post(self , request):
        #serializer = UserSerializer(data = request.data)
        #if not serializer.is_valid():
            #return Response({'status' :403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})
        #serializer.save()

        #user = User.objects.get(username = serializer.data['username'])
        #token_obj , _ = Token.objects.get_or_create(user=user)

        #return Response({'status' :200 , 'payload' : serializer.data ,'token' : str(token_obj) ,'message' : 'Your data is saved'})