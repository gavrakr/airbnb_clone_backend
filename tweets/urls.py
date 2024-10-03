from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweets),
    path("tweets_board", views.tweets_board),
]
