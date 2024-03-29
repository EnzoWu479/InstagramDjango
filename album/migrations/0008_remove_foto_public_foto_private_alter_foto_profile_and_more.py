# Generated by Django 4.0.6 on 2022-07-25 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0007_foto_publishdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='public',
        ),
        migrations.AddField(
            model_name='foto',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='foto',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='foto',
            name='publishData',
            field=models.DateTimeField(blank=True),
        ),
    ]
