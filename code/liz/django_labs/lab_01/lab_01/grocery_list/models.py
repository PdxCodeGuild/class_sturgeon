from django.db import models
from django.utils import timezone


# Create your models here.
class GroceryItem (models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
    