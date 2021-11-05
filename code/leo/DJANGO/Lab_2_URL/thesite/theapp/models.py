
from django.db import models


class Encoder(models.Model):

    url = models.CharField(max_length=30)
    Date_Added = models.DateTimeField(auto_now_add=True, null=True)
    code = models.CharField(max_length=30)
    
   
    def __str__(self):
        return self.url