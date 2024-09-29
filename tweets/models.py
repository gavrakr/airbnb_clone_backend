from django.db import models
from users.models import User
from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.payload


class Link(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.tweet)
