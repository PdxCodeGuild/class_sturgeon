# Generated by Django 3.2.9 on 2021-11-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='unkown', max_length=30),
        ),
    ]
