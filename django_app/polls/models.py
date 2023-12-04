from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)


class Question(models.Model):
    """Question model"""
    name = models.CharField(max_length=512)
    question_text = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)


class Choice(models.Model):
    """Choice model - Foreign Key to Question model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# done
