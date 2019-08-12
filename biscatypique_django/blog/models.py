from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    link = models.URLField(default='http://salut.com')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    adress = models.TextField()
    price = models.CharField(max_length=5)
    starthour = models.TimeField()
    endhour = models.TimeField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.TextField()
    occasion = models.TextField()
    link = models.URLField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})