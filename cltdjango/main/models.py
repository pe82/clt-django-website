from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateJoined = models.DateTimeField()
    githubUrl = models.URLField()
    linkedInUrl = models.URLField()
    photo = models.URLField()
