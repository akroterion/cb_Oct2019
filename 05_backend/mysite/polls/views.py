from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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
    q1 = get_object_or_404(Question, pk=question_id)

    try:
        c1 = q1.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            'title': q1.question_text,
            'question': q1,
            'error_message': "Nie wybrałeś odpowiedzi!",
        })
    else:
        c1.votes += 1
        c1.save()
        return redirect(reverse('results', args=[q1.pk]))
        # return redirect('results', question_id=q1.pk)

# /polls/<question_id>/results/
def results(request, question_id):
    q1 = get_object_or_404(Question, pk=question_id)
    context = {
        'title': q1.question_text,
        'question': q1,
    }
    return render(request, "polls/results.html", context)
