# Generated by Django 3.2.8 on 2021-11-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_auto_20211101_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='short',
            name='user_ip',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
