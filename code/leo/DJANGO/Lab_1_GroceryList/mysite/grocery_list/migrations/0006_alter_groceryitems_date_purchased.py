# Generated by Django 3.2.9 on 2021-11-01 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0005_auto_20211101_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitems',
            name='Date_Purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
