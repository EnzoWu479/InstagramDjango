# Generated by Django 4.0.6 on 2022-07-27 00:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0009_alter_foto_publishdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='comments',
        ),
        migrations.AddField(
            model_name='foto',
            name='likes',
            field=models.ManyToManyField(related_name='foto_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
