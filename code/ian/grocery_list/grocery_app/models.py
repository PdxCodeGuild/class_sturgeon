from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone
from datetime import datetime

# Create your models here.
class GroceryItem(models.Model):
    name = models.CharField(max_length=50) 
    pub_date = models.DateTimeField(auto_now_add=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
