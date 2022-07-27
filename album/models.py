from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Foto(models.Model):
    photo = models.ImageField(upload_to='photos/%Y-%m-%d', default='defaultPhoto.jpg')
    description = models.TextField(max_length=255, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    private = models.BooleanField(default=False)
    publishData = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User)

    def __str__(self):
        return self.description


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile/%Y-%m-%d', default='defaultUser.jpg')
    description = models.TextField(max_length=255, blank=True)

@receiver(post_save, sender=User)
def create_usr_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()