from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Create your models here.

class TipModel(models.Model):

    content = models.TextField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    upvoter = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="upvoter_users")
    downvoter = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="downvoter_users")


    class Meta:
        permissions = [
            ("can_downvote", "Can Downvote"),
        ]

    def __str__(self):
        return self.author.username
    

class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)
