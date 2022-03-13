from statistics import mode
from tkinter import CASCADE
from django.db import models




class Boss(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    address = models.IntegerField()


class Employee(models.Model):
    employee = models.ForeignKey(Boss, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age =  models.IntegerField()


