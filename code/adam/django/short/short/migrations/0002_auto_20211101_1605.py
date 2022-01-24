# Generated by Django 3.2.8 on 2021-11-01 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='short',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='short',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]