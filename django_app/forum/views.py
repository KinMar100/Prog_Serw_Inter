from django.shortcuts import render
from django.http import HttpResponse as HttpR, HttpResponseBase


def home(request) -> HttpResponseBase:
    return render(request, 'home.html')


def subpage(request) -> HttpResponseBase:
    return render(request, 'subpage.html')
