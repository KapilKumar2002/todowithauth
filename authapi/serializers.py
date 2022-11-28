from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UsersTodo
class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UsersTodo
        fields = "__all__"
class AuthSerializer(serializers.ModelSerializer):
    user_todo = TodoSerializer(many = True,read_only = True)
    class Meta:
        model = User
        fields = ["id",'username',"email","password","user_todo"]