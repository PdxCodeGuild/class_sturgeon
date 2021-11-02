from django.db import models
from django.utils import timezone

# Create your models here.
class user_list(models.Model):
    grocery = models.TextField(max_length=50)
    amount = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now())

