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
    def __str__(self):
        return f'{self.user} Neighborhood'

    class Meta:
        db_table ='Neighborhood'

class Profile(models.Model):
    name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.user} Profile'

    class Meta:
        db_table ='Profile'

class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} Business'

    class Meta:
        db_table ='Business'


    @classmethod
    def search_by_id(cls,search_term):
        business = cls.objects.filter(id__icontains=search_term)
        return business
