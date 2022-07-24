from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
class Foto(models.Model):
    photo = models.ImageField(upload_to='media/photos/%Y-%m-%d', blank=True)
    description = models.TextField(max_length=255)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = ArrayField(models.TextField(max_length=100), default=[])
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.description