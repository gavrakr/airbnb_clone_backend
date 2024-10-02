from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


def all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "tweet.html",
        {
            "title": "Tweet Board",
            "tweets": tweets,
        },
    )
