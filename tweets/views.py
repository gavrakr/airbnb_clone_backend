from django.shortcuts import render
from django.http import HttpResponse


def all_tweets(request):
    return HttpResponse("all_tweets")
