from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

urlpatterns = [
      path("",admin_required(home.as_view()),name="home"),
      path("tiktok",admin_required(tiktok.as_view()),name="tiktok"),
      path("about",views.About,name="about"),
      path("contact",views.Contact,name="contact"),
      path("terms",views.Terms,name="terms"),
  ]
