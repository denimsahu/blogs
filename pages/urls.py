from django.urls import path,include
from pages import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path("logout",views.logout_user,name='logout'),
    path("contact/",views.contact_us,name="contact"),
    path("home/blog/",views.blog,name="blog"),
    path("home/edit/",views.edit,name="edit_blog"),
    #remove experiment at end
    path("experiment/",views.experiment,name="experiment"),
]
