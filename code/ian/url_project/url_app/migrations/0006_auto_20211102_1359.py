# Generated by Django 3.2.8 on 2021-11-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0005_auto_20211101_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='computer_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='os',
            field=models.TextField(blank=True, null=True),
        ),
    ]