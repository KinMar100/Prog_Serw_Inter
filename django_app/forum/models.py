from django.db import models

# Create your models here.


class Rank(models.Model):
    # host =
    # topic =
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True, blank=True)
    # users =
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    # user =
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL)
