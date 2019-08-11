from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    adress = models.TextField()
    price = models.CharField(max_length=5)
    starthour = models.TimeField()
    endhour = models.TimeField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.TextField()
    occasion = models.TextField()
    link = models.URLField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    