# Generated by Django 3.2.8 on 2021-10-25 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
