from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

class Post(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    desc= models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=70)
    technologies = models.CharField(max_length=100)