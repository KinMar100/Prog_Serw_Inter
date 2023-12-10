from django.db import models

from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    """Question model"""
    name = models.CharField(max_length=512)
    question_text = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    user_question = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Choice(models.Model):
    """Choice model - Foreign Key to Question model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    user_choice = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'ID = {self.id}'


# done
