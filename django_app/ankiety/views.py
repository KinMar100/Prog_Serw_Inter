from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as HttpR, Http404

from .models import Pytanie, Wybor


# Create your views here.


def index(request) -> HttpR:
    return HttpR("Indeks ankiet")


def szczegoly(request, pytanie_id) -> HttpR:
    try:
        pytanie = Pytanie.objects.get(pk=pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404("Takie pytanie nie istnieje.")
    return render(request, {"question": pytanie})


def wynik(request, pytanie_id) -> HttpR:
    try:
        pytanie = Pytanie.objects.get(pk=pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404("Takie pytanie nie istnieje.")
    return render(request, {"question": pytanie})
    # return HttpR("Wyszukiwanie wyniku dla pytania: {}".format(pytanie_id))


def glos(request, pytanie_id) -> HttpR:
    question = get_object_or_404(Pytanie, pk=pytanie_id)
    try:
        wybrany_wybor = pytanie_id.choice_set.get(pk=request.POST["wybor"])
    except (KeyError, Wybor.DoesNotExist):
        return render(request, {"pytanie": question, "error_message": "Nie wybrano wyboru."},)
    else:
        wybrany_wybor.votes += 1
        wybrany_wybor.save()
    # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
