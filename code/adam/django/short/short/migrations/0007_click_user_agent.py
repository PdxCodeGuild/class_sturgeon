# Generated by Django 3.2.8 on 2021-11-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0006_click_remote_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='user_agent',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
