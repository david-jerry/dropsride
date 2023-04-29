from rest_framework import exceptions, serializers

from dropsride.settings.models import CarType, Localization, Promo, PromoUsage


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


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = [
            "id",
            "name",
            "code",
            "usage_count",
            "rides_count",
            "description",
            "discount_rides",
            "discount_percent",
            "start_date",
            "end_date",
            "is_active",
        ]


class PromoSubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoUsage
        fields = ["id", "promo", "subscriber", "used", "used_date"]
