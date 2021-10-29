from django.db import models

# Create your models here.

class Short(models.Model):
    user_url = models.URLField(max_length=200)
    new_url = models.CharField(max_length=15)
