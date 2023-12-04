from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as HttpR, Http404

from .models import Question, Choice


# Create your views here.


def index(request) -> HttpR:
    return HttpR("Polls index")


# def details(request, question_id) -> HttpR:
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, {"question": question})
#
#
# def result(request, question_id) -> HttpR:
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, {"question": question})
#
#
# def vote(request, question_id) -> HttpR:
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         chosen_quest = question_id.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, {"question": question, "error_message": "No Choice selected."},)
#     else:
#         chosen_quest.votes += 1
#         chosen_quest.save()
