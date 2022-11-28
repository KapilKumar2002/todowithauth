from rest_framework import generics

# Create your views here.
from django.contrib.auth.models import User
from .models import UsersTodo
from .serializers import AuthSerializer, TodoSerializer


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer



class ReadUpdateDeleteUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer


class Todos(generics.ListCreateAPIView):
    queryset = UsersTodo.objects.all()
    serializer_class = TodoSerializer
class TodosRUDs(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersTodo.objects.all()
    serializer_class = TodoSerializer