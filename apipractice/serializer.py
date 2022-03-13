from dataclasses import fields
from rest_framework import serializers
from .models import Employee,Boss


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss 
        fields='__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
    employee =  BossSerializer()
    class Meta:
        model = Employee
        fields='__all__'