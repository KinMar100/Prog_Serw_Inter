import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    """Question model"""
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("publication")

    def __str__(self) -> str:
        return self.question_text

    def publication_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Choice model - Foreign Key to Question model"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

# done
