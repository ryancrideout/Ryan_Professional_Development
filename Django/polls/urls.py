from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # example: /polls/
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    # example: /polls/<id>/
    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # example: /polls/<id>/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # example: /polls/<id>/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]