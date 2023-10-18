from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "myApp/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myApp/detail.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "myApp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now())

class DetailView(generic.DetailView):
    model = Question
    template_name = "myApp/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "myApp/results.html"

class question():
    def detail(request, question_id):
        return HttpResponse(f"You're looking at question {question_id}")
    
    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/results.html", {"question": question})
    
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                "myApp/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice"
                }
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))