import datetime

from django.db import models
from django.utils import timezone
# Create your models here. 
# For futher reference: https://docs.djangoproject.com/en/3.2/intro/tutorial02/
# We put models.Model to take Django's Model and say "yes, and..."
# image_field is used for like putting two pictures and html is where you do the swipe left or right
# the max_length on the CharField of 200 is a normal suggestion, you can limit to 9 for social security, for example
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text