from django.contrib.auth import get_user_model
from rest_framework import serializers

from dropsride.currency.models import Banks, Currency, States


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "code", "symbol", "price"]


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ["id", "state", "country_iso"]


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ["name", "slug", "lcode", "code", "country_iso"]

        extra_kwargs = {"url": {"view_name": "api:bank-detail", "lookup_field": "slug"}}
