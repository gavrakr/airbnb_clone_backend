from django.db import models
from users.models import User


class Tweet(models.Model):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField()
    update_at = models.DateField()

    def __str__(self):
        return self.payload


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.SET_NULL, null=True)
    create_at = models.DateField()
    update_at = models.DateField()

    def __str__(self):
        return str(self.tweet)
