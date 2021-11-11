from django.db import models
from django.urls import reverse

# Create your models here.
class Post (models.Model):
    chirp = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.chirp}, {self.author}"

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))
    
    class Meta:
        ordering = ['-created']