# Generated by Django 3.2 on 2021-12-02 19:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='caught_by',
            field=models.ManyToManyField(blank=True, related_name='caught', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image_back',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image_front',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]