from django.conf import settings
from rest_framework import serializers

from dropsride.settings.api.serializers import LocalizationSerializer

from ..models import TicketPlans, TicketSubscription


class SubscriptionPlansSerializer(serializers.ModelSerializer):
    localization = LocalizationSerializer(many=False, read_only=True)

    class Meta:
        model = TicketPlans
        fields = [
            "localization",
            "interval",
            "duration",
            "amount",
        ]
        read_only_fields = [
            "amount",
        ]


class DriverSubscriptionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = TicketSubscription
        fields = [
            "id",
            "username",
            "driver",
            "status",
            "plan",
            "active",
            "expiry_date",
            "url",
        ]

        read_only_fields = [
            "id",
            "username",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:subscription-detail", "lookup_field": "id"}
        }

    def get_username(self, obj):
        return obj.driver.username
