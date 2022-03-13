from django.contrib import admin
from django.urls import path
from apipractice.views import UserDetails,user_data

urlpatterns = [
    path('userdetails/',UserDetails.as_view(),name='userdetails'),
    path("user_data",user_data,name="user_data")
]