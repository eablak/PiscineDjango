from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipModel(models.Model):

    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    upvoter = models.ManyToManyField(User, related_name="upvoter_users")
    downvoter = models.ManyToManyField(User, related_name="downvoter_users")


    def __str__(self):
        return self.author.username