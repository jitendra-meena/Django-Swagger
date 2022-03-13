from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Employee
from .serializer import UserDetailsSerializer
import json
import requests

class UserDetails(APIView):
    def get(self,request):
        college = Employee.objects.all()
        serializer = UserDetailsSerializer(college,many=True)  
        return Response(serializer.data) 


def user_data(request):
    response=requests.get('http://127.0.0.1:8000/userdetails/').json()
    return render(request,'user.html',{'response':response})