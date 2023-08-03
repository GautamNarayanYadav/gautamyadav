from django.db import models


class MyProfile(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
