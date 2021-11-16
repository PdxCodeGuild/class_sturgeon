from django.db import models

# Create your models here.

class Items(models.Model):
    content = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.content} {self.complete}"