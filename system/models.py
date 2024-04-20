from django.contrib.auth.models import User
from django.db import models

from accounts.models import ModelMixin


class MyProfile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    intro = models.CharField(max_length=100)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    date = models.DateTimeField(blank=True)
    image1 = models.ImageField(upload_to='blogs/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.intro

