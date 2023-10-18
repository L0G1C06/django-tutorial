from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter
from .views import index, question, IndexView, DetailView, ResultsView, GetMethod

app_name = "polls"
router = DefaultRouter()
router.register("data", GetMethod, basename="data")
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", question.vote, name="vote"),
    re_path(r'^api/', include((router.urls))),
]