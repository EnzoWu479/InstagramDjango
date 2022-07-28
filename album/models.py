from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_resized import ResizedImageField

class Foto(models.Model):
    photo = models.ImageField(upload_to='photos/%Y-%m-%d', default='defaultPhoto.jpg')
    photo_512 = ResizedImageField(size=[1024, 1024], crop=['middle', 'center'], upload_to='photos/%Y-%m-%d/size512', default="")
    description = models.TextField(max_length=255, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    private = models.BooleanField(default=False)
    publishData = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='foto_post')
    def __str__(self):
        return self.description


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile/%Y-%m-%d', default='defaultUser.jpg')
    photo_100 = ResizedImageField(size=[200, 200], crop=['top', 'center'], upload_to="profile/%Y-%m-%d/size100", default="")
    photo_256 = ResizedImageField(size=[512, 512], crop=['top', 'center'], upload_to="profile/%Y-%m-%d/size256", default="")
    description = models.TextField(max_length=255, blank=True)
    saved = models.ManyToManyField(Foto, related_name="saved_post")

@receiver(post_save, sender=User)
def create_usr_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()