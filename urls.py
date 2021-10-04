from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Tasks/',views.Tasks,name="about"),
]