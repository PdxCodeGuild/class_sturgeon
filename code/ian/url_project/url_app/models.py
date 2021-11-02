from django.db import models

# Create your models here.
class UrlItem(models.Model):
    long = models.TextField()
    # use code generator for short code (6 digit)
    short = models.TextField(blank=True, null=True)
    clicks = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.long

class Click(models.Model):
    username = models.TextField(blank=True, null=True)
    computer_name = models.TextField(blank=True, null=True)
    os = models.TextField(blank=True, null=True)
    urlitem = models.ForeignKey(UrlItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.urlitem
