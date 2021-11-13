from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self')

class OnlyPlan(models.Model):
    owner = models.CharField(max_length=150)
    title = models.CharField(max_length=280, verbose_name="Titill")
    location_latitude = models.CharField(max_length=20, default="", verbose_name="Breiddargráða")
    location_longitude = models.CharField(max_length=20, default="", verbose_name="Lengdargráða")
    reach = models.IntegerField(verbose_name="Umfang")
    when = models.DateTimeField(verbose_name="Tímasetning")
    duration = models.IntegerField(verbose_name="Hve lengi?")
    friendsonly = models.BooleanField(verbose_name="Bara fyrir vini", default=False)
