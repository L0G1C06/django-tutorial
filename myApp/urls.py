from django.urls import path 

from .views import index, question, IndexView, DetailView, ResultsView

app_name = "polls"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", question.vote, name="vote"),
]