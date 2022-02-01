from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
# Create your views here.
def registerpage (request):
    print(request.method)
    print('check')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        print('check2')
        if form.is_valid():
            print('TRUE')
            form.save()
            messages.success(request,'your account has been created !!you are now able to log in ')
        else:
            print("false")
    else:
        print('FALSE')
        form = RegisterForm()
    return render(request,'Register.html',{'form':form})

def loginpage (request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

def log_out(request):
    auth.logout(request)
    return redirect('/login')


