# Generated by Django 3.2.9 on 2021-11-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urldb',
            name='short_url',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
