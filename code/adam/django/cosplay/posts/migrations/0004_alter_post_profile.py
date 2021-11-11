# Generated by Django 3.2.8 on 2021-11-04 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_phone_number'),
        ('posts', '0003_auto_20211104_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='users.profile'),
        ),
    ]