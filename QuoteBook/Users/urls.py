from django.contrib import admin
from django.urls import path, include
from . import register


urlpatterns = [
    path('', views.register, name = "user registration"),
    path('register/', views.register, name = "user registration"),
]
