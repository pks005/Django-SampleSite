from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email, self.username, self.timestamp
