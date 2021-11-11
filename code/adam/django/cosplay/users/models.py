from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', related_name='followers', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def posts_count(self):
        return len(self.posts.all())

    @property
    def followers_count(self):
        print(self.followers.all())
        return len(self.followers.all())
    @property
    def following_count(self):
        print(self.following.all())
        return len(self.following.all())

    def __str__(self):
        return self.user.username
