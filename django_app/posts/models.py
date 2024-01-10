from typing import Tuple

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
    reaction_like = models.ManyToManyField(User, related_name='reactions_like')
    reaction_dislike = models.ManyToManyField(User, related_name='reactions_dislike')

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


    def view_object(self) -> str:
        return f'{self.user}"\n"{self.description}'


class Reaction(models.Model):
    LIKE = 'like'
    LOVE = 'love'
    DISLIKE = 'dislike'

    REACTION_CHOICE = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (DISLIKE, 'Dislike')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type_of_reaction = models.CharField(max_length=20, choices=REACTION_CHOICE)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} reacted with \'{self.type_of_reaction}\' to {self.post}'
