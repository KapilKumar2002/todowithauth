from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UsersTodo(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_todo")
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=350)

    def __str__(self):
        return str(self.owner)