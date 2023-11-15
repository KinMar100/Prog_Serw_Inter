from django.shortcuts import render
from django.http import HttpResponse as HttpR, HttpResponseBase

from .models import Rank

# ranks = [
#    {'id': 1, 'name': 'first'},
#    {'id': 2, 'name': 'second'},
#    {'id': 3, 'name': 'third'},
# ]


def home(request) -> HttpResponseBase:
    ranks = Rank.objects.all()
    # wszystkie rangi w bazie
    context = {'ranks': ranks}
    return render(request, 'home.html', context)


def subpage(request, pk) -> HttpResponseBase:
    rank = Rank.objects.get(id=pk)
    context = {'rank': rank}
    return render(request, 'subpage.html', context)
