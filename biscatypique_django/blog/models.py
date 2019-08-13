from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    previewtext = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    link = models.URLField(default='http://salut.com')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        img.save(self.image.path)

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    adress = models.TextField()
    price = models.CharField(max_length=5)
    starthour = models.TimeField()
    endhour = models.TimeField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        img.save(self.image.path)

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default="01/01/2001")
    location = models.TextField(default="rien")
    occasion = models.TextField(default="rien")
    link = models.URLField(default="http://salut.com")
    image = models.ImageField(upload_to='profile_pics')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog-saved_gallery')

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        img.save(self.image.path)