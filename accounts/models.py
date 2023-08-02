from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from accounts.choices import *


class ModelMixin(models.Model):
    """
        This mixins provide the default field in the models project wise
    """
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created",
                                   on_delete=models.CASCADE, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_updated",
                                   on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, default='active', choices=STATUS_TYPE, help_text=_('Status'))

    def __str__(self):
        return self.created_by.email

    class Meta:
        abstract = True


class Profile(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.FileField(upload_to='user/profile', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER, default='Male')
    role = models.CharField(max_length=100, choices=ROLE, null=True, blank=True)
    Skill = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)

    def __str__(self):
        return self.name
