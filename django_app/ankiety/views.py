from django.shortcuts import render
from django.http import HttpResponse as HttpR

# Create your views here.


def index(request):
    return HttpR("Indeks ankiet")
