from django.db import models

# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    cohort = models.CharField(max_length=250)
    favoriteTopic = models.CharField(max_length=250)
    favoriteTeacher = models.CharField(max_length=250)
    capstone = models.URLField(max_length=500)

    def __str__(self):
        return self.firstName