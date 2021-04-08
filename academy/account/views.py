from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        u=User.objects.filter(username=username)
        if u.exists():
            messages.warning(request,'xatolik')
            return redirect('account:register')
        else:
            user1=User(username=username,email=email,password=make_password(password))
            user1.save()
            return redirect('account:login')
    return render(request,'account/register.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home:homepage')
    return render(request,'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:homepage')

