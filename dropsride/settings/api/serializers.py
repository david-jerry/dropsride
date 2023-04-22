from rest_framework import exceptions, serializers

from dropsride.settings.models import CarType, Localization


class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = [
            "uuid",
            "state",
            "tiket_fare",
            "base_price",
            "cost_per_km",
            "cost_per_15min",
            "url",
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {
            "url": {"view_name": "api:localization-detail", "lookup_field": "uuid"}
        }


class CartypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ["image", "slug", "title", "amount", "seats", "url"]
        read_only_fields = ["slug"]
        extra_kwargs = {
            "url": {"view_name": "api:cartype-detail", "lookup_field": "slug"}
        }
