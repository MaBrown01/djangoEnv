from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validateUser(self, post):
        print post

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Objects = UserManager()
