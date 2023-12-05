from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
      path("",home.as_view(),name="home"),
      path("tiktok",tiktok.as_view(),name="tiktok"),
      path("about",views.About,name="about"),
      path("contact",views.Contact,name="contact"),
      path("terms",views.Terms,name="terms"),
  ]
