from django.db import models
from django.urls import reverse

from users.models import User


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def abs_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField(default='')
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
