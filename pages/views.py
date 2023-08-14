from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from pages.models import *
from datetime import datetime

edit_this_blog=""

def login_page(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('home')
       else:
            return redirect('login_page')
    return render(request,'login.html')


def home(request):
    user_name = str(request.user)
    
    if request.user.is_authenticated:
        data = blogs.objects.all()

        if request.method == "POST":
            selected_blog_id = request.POST.get("selected_blog")
            delete_blog_id = request.POST.get("delete_blog")
            edit_blog_id=request.POST.get("edit_blog")
            
            
            if delete_blog_id:
                delete_this=blogs.objects.get(pk=delete_blog_id)
                delete_this.delete()
                delete_blog_id=None

            elif edit_blog_id:
                global edit_this_blog
                edit_this_blog=blogs.objects.get(pk=edit_blog_id)
                return redirect('edit_blog')
            
            else:
                selected_blog = blogs.objects.get(pk=selected_blog_id)
                selected_blog_blog = str(selected_blog.blog)
                selected_blog_title = str(selected_blog.title)
                return render(request, 'home.html', {'data': data,'selected_blog':selected_blog ,'user_name': user_name, 'blog_title': selected_blog_title, 'blog_content': selected_blog_blog, 'blog_author': selected_blog.username,})
        
        return render(request, 'home.html', {'data': data, 'user_name': user_name})
    else:
        return redirect('login_page')

def logout_user(request):
    logout(request)
    return redirect('login_page')

def edit(request):
    if request.user.is_authenticated:
       if request.method=="POST":
           content=request.POST.get("blog")
           edit_this_blog.blog=content
           edit_this_blog.save()
           return redirect('home')
       return render(request,"edit_blog.html",{'blog':edit_this_blog})
    else:
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


def experiment(request):
    return render(request,'experiment.html')



