import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


# model - Question
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("publication")

    def __str__(self) -> str:
        return self.question_text

    def publicated_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# model - Choice (Klucz obcy do modelu - Question)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
