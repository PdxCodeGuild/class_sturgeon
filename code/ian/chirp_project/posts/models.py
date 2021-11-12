from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(max_length=280)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:details", args=(self.pk,))

    class Meta:
        ordering=["-created"]

class Comments(models.Model):
    post_item = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    users_liked = models.ManyToManyField(User)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.post_item