# Generated by Django 3.2.9 on 2021-11-08 20:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_auto_20211108_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='users_liked',
        ),
        migrations.AddField(
            model_name='comments',
            name='users_liked',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
