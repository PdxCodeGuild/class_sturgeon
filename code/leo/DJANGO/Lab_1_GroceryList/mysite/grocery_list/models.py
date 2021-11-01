import datetime
from django.db import models
from django.utils import timezone

class GroceryItems(models.Model):


    Item_Name = models.CharField(max_length=30)
    Date_Added = models.DateTimeField()
    Purchased = models.BooleanField()
    Date_Purchased = models.DateTimeField(null=True, blank=True)
   

    def __str__(self):
        return self.Item_Name