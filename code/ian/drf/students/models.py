from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    cohort = models.CharField(max_length=250)
    favorite_topic = models.CharField(max_length=250)
    favorite_teacher = models.CharField(max_length=250)
    capstone = models.URLField()

    def __str__(self):
        return self.first_name