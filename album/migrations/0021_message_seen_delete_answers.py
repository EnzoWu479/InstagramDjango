# Generated by Django 4.0.6 on 2022-08-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0020_message_datatime'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]