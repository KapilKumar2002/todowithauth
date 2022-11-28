from django.urls import path
from .views import CreateUser, ReadUpdateDeleteUser,Todos, TodosRUDs
urlpatterns = [
    path("",CreateUser.as_view()),
    path("<int:pk>",ReadUpdateDeleteUser.as_view()),
    path("todos/",Todos.as_view()),
    path("todos/<int:pk>",TodosRUDs.as_view()),
]