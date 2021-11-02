from django.db import models



class UrlDb (models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=6)

    def __str__ (self):
        return f"{self.short_url}, {self.long_url}"

    