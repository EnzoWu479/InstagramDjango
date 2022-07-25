from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Foto(models.Model):
    photo = models.ImageField(upload_to='photos/%Y-%m-%d', default='defaultPhoto.jpg')
    description = models.TextField(max_length=255, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    comments = ArrayField(models.TextField(max_length=100), default=list)
    public = models.BooleanField(default=True)
    publishData = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile/%Y-%m-%d', default='defaultUser.jpg')

@receiver(post_save, sender=User)
def create_usr_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()