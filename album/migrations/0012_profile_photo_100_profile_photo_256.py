# Generated by Django 4.0.6 on 2022-07-27 21:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0011_profile_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo_100',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[100, 100], upload_to='profile/%Y-%m-%d/size100'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo_256',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[256, 256], upload_to='profile/%Y-%m-%d/size256'),
        ),
    ]
