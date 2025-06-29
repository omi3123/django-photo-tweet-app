from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TweetModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='photos/')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    