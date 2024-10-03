from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from tweets.serializers import TweetSerializer
from .models import User


@api_view()
def user_tweets(request, user_id):
    try:
        user = User.objects.get(username=user_id)
        all_tweets = user.tweets.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"ok": False})


@api_view()
def user(request, user_id):
    try:
        user = User.objects.get(username=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"ok": False})


@api_view()
def users(request):
    all_users = User.objects.all()
    serializer = UserSerializer(
        all_users,
        many=True,
    )
    return Response(serializer.data)
