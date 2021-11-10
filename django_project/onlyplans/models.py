from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class OnlyPlan(models.Model):
    owner = models.CharField(max_length=150)
    title = models.CharField(max_length=280, verbose_name="Titill")
    location_latitude = models.CharField(max_length=20, default="", verbose_name="Breiddargráða")
    location_longitude = models.CharField(max_length=20, default="", verbose_name="Lengdargráða")
    reach = models.IntegerField(verbose_name="Umfang")
    when = models.DateTimeField(verbose_name="Tímasetning")
    duration = models.IntegerField(verbose_name="Hve lengi?")
    friendsonly = models.BooleanField(verbose_name="Bara fyrir vini", default=False)

class FriendMgmt(models.Model):
    """
        friends table
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friends", on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()