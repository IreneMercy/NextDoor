from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.http import Http404

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    occupants = models.IntegerField()


class Profile(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    image = models.ImageField()
