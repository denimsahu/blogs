from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from pages.models import *
from datetime import datetime


def login_page(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('home')
       else:
            return redirect('login.html')
    return render(request,'login.html')


def home(request):
    if request.user.is_authenticated:
        data=blogs.objects.all()
        return render(request,'home.html',{'data':data})
    else:
        return redirect('login_page')

def logout_user(request):
    logout(request)
    return redirect('login_page')



def contact_us(request):
    if request.user.is_authenticated:
        return render(request,"contact.html")
    else:
        return redirect('login_page')


def blog(request):
    if request.method=='POST':
        username=request.user
        title=request.POST.get('title')
        blog=request.POST.get('blog')
        Blog=blogs(title=title,blog=blog,date_time=datetime.now(),username=username)
        Blog.save()
        return redirect('home')

    if request.user.is_authenticated:
        return render (request,'blog.html')
    else:
        return redirect('login_page')

def signup(request):
    if request.method=='POST':
      username=request.POST.get('new-user-username')
      password1=request.POST.get('new-user-password1')
      password2=request.POST.get('new-user-password2')
      if (password1!=password2):
         return redirect('signup')
      else:
         User.objects.create_user(username=username,password=password1)
         return redirect('login_page')
    return render(request,'signup.html')






