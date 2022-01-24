from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description: models.CharField(max_length=200)
    created: models.DateTimeField()
    competed: models.DateTimeField(null=True, blank=True)
    delete: models.BooleanField()

    def __str__(self):
        return self.description
