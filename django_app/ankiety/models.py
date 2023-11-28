import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


# model - Pytanie
class Pytanie(models.Model):
    pytanie_tresc = models.CharField(max_length=250)
    data_publikacji = models.DateTimeField("opublikowane")

    def __str__(self) -> str:
        return self.pytanie_tresc

    def czy_opublikowane_niedawno(self) -> bool:
        return self.data_publikacji >= timezone.now() - datetime.timedelta(days=1)


# model - Wybor (Klucz obcy do modelu - Pytanie)
class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    wybor_tresc = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.wybor_tresc
