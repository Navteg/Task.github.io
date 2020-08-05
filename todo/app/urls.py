from django.contrib import admin
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('app/sign_up/',views.sign_up,name="sign-up"),
    path('app/login',auth_views.LoginView.as_view(template_name="app/login.html"),name="login"),
    path('app/logout',auth_views.LoginView.as_view(template_name="app/logged_out.html"),name="logout"),
]
