from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
