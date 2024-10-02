from django.shortcuts import render
from .models import Tweet


def tweets_board(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "tweet.html",
        {
            "title": "Tweet Main Page",
            "tweets": tweets,
        },
    )
