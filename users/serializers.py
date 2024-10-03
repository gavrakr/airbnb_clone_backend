from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        read_only=True,
    )
    username = serializers.CharField(read_only=True)

    first_name = serializers.CharField(
        read_only=True,
    )
    last_name = serializers.CharField(
        read_only=True,
    )
    name = serializers.CharField(
        max_length=150,
    )
    is_hosts = serializers.BooleanField()
    gender = serializers.ChoiceField(
        choices=User.GenderChoices.choices,
    )
    language = serializers.ChoiceField(
        choices=User.LanguageChoices.choices,
    )
    currency = serializers.ChoiceField(
        choices=User.CurrencyChoices.choices,
    )
