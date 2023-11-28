from django.db import models

# Create your models here.


class Pytanie(models.Model):
    pytanie_tresc = models.CharField(max_length=250)
    data_publikacji = models.DateTimeField("opublikowane")


class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    wybor_tresc = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)
