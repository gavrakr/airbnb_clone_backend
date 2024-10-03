from django.urls import path
from . import views

urlpatterns = [
    path("", views.users),
    path("<str:user_id>", views.user),
    path("<str:user_id>/tweets", views.user_tweets),
]
