from django.db import models

class student(models.Model):
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Favorite_Topic = models.CharField(max_length=100)
    Capstone = models.URLField(max_length=100)

    def __str__(self):
        return self.First_Name
