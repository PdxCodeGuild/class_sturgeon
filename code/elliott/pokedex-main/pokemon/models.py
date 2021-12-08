from django.db import models
from django.contrib.auth import get_user_model

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    image_front = models.URLField(blank=True, null=True)
    image_back = models.URLField(blank=True, null=True)
    caught_by = models.ManyToManyField(get_user_model(), related_name='caught',blank=True)
    # types = the set of Types associated with that Pokemon

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')

    def __str__(self):
        return self.type
    
