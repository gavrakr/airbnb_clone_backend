from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer


@api_view(["GET"])
def tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(
        all_tweets,
        many=True,
    )
    return Response(serializer.data)


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
