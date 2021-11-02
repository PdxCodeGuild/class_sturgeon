from django.db import models

# Create your models here.

class Short(models.Model):
    user_url = models.URLField(max_length=200)
    new_url = models.CharField(max_length=15)
    # here I'm trying to expancd the database to include time created
    created = models.DateTimeField(auto_now_add=True)
    user_ip = models.CharField(max_length=50)
    times_used = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["-created"]

# class Click(models.Model):
#     short_meta = models.ForeignKey(Short, on_delete=models.CASCADE)