from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=50)
    fav_topic = models.CharField(max_length=50)
    fav_teacher = models.CharField(max_length=50)
    capstone = URLField(max_length=200)
    

    def __str__(self):
        return self