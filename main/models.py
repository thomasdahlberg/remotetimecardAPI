from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_user = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Site(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    radius = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class TimePunch(models.Model):
    punch_time: models.DateTimeField("Punch Time")
    lat = models.FloatField()
    lng = models.FloatField()
    proximity = models.FloatField()
    verified = models.BooleanField(default=False)

class Session(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    punch_in: models.ForeignKey(TimePunch, on_delete=models.CASCADE)
    punch_out: models.ForeignKey(TimePunch, on_delete=models.CASCADE)





    
