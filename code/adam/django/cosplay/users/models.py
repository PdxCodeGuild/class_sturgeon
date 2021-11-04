from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# from autoslug import AutoSlugField
# from posts.models import Post

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', related_name='followers', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    # friends = models.ManyToManyField("Profile", blank=True)
    # slug = AutoSlugField(populate_from='user')
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

    def followers_count(self):
        return len(self.followers.all())

    def followering_count(self):
        return len(self.following.all())

    def __str__(self):
        return self.user.username



#     def get_absolute_url(self):
#         return "/users/{}".format(self.slug)

#     def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#         if created:
#             try:
#                 Profile.objects.create(user=instance)
#             except:
#                 pass

#     post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

# class FriendRequest(models.Model):
# 	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
# 	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
# 	timestamp = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return "From {}, to {}".format(self.from_user.username, self.to_user.username)
