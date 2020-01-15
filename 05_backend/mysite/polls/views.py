from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

# /polls/
def index(request):
    questions = Question.objects.all().order_by('-pub_date')
    context = {
        'title': 'Ankiety',
        'questions': questions,
    }
    return render(request, "polls/index.html", context)


# /polls/<question_id>/
def details(request, question_id):
    q1 = get_object_or_404(Question, pk=question_id)
    context = {
        'title': q1.question_text,
        'question': q1,
    }
    return render(request, "polls/details.html", context)


# /polls/<question_id>/vote/
def vote(request, question_id):  # metoda POST
    pass


# /polls/<question_id>/results/
def results(request, question_id):
    q1 = get_object_or_404(Question, pk=question_id)
    context = {
        'title': q1.question_text,
        'question': q1,
    }
    return render(request, "polls/results.html", context)
