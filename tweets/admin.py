from django.contrib import admin
from .models import Tweet, Link


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "user", "create_at", "update_at")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet", "create_at", "update_at")
