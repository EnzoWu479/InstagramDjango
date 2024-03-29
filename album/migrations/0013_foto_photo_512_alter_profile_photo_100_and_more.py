# Generated by Django 4.0.6 on 2022-07-27 23:29

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0012_profile_photo_100_profile_photo_256'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='photo_512',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1024, 1024], upload_to='photos/%Y-%m-%d/size512'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_100',
            field=django_resized.forms.ResizedImageField(crop=['top', 'center'], default='', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[200, 200], upload_to='profile/%Y-%m-%d/size100'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_256',
            field=django_resized.forms.ResizedImageField(crop=['top', 'center'], default='', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[512, 512], upload_to='profile/%Y-%m-%d/size256'),
        ),
    ]
