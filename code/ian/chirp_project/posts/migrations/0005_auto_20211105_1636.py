# Generated by Django 3.2.9 on 2021-11-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211104_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=280),
        ),
    ]
