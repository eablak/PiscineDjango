from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)


class UserMessage(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

class ChatRoomUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)