from datetime import datetime, timedelta
from decimal import Decimal

import googlemaps
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from humanfriendly import format_length, format_timespan

from dropsride.settings.models import CarType, Localization
from dropsride.tickets.models import TicketSubscription

from ..models import Rating, Trips  # , Waypoint1, Waypoint2 #Riders

gmaps = googlemaps.Client(key=settings.GOOGLE_API)

from rest_framework import exceptions, serializers


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "user", "trip", "rating", "modified"]
        read_only_fields = [
            "id",
        ]


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = [
            "uuid",
            "user",
            "driver",
            "pickup",
            "state",
            "p_point",
            "dropoff",
            "d_point",
            "pay_method",
            "driver_arrived",
            "depature_time",
            "arrival_time",
            "arrived_at",
            "fmt_sec",
            "distance_km",
            "amount",
            "waypoint1_address",
            "waypoint1_point",
            "waypoint2_address",
            "waypoint2_point",
            "car_type",
            "gross_total",
            "status",
            "active",
            "url",
        ]
        read_only_fields = ["uuid"]
        extra_kwargs = {"url": {"view_name": "api:trip-detail", "lookup_field": "uuid"}}

    # def update(self, instance, validated_data):
    #     car_type = CarType.objects.get(id=int(validated_data.get('car_type')))
    #     new_amount = instance.amount + car_type.amount

    #     p_point = Point(Decimal(validated_data.get('p_point_longitude')), Decimal(validated_data.get('p_point_latitude')), srid=4326)
    #     w1_point = Point(0.0, 0.0)
    #     w2_point = Point(0.0, 0.0)
    #     if validated_data.get('waypoint1_point_longitude') and not validated_data.get('waypoint2_point_longitude'):
    #         w1_point = Point(Decimal(validated_data.get('waypoint1_point_longitude')), Decimal(validated_data.get('waypoint1_point_latitude')), srid=4326)
    #         # res = gmaps.distance_matrix(
    #         #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
    #         #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
    #         # )
    #     elif validated_data.get('waypoint2_point_longitude'):
    #         w2_point = Point(Decimal(validated_data.get('waypoint2_point_longitude')), Decimal(validated_data.get('waypoint2_point_latitude')), srid=4326)
    #         w1_point = Point(Decimal(validated_data.get('waypoint1_point_longitude')), Decimal(validated_data.get('waypoint1_point_latitude')), srid=4326)
    #         # res = gmaps.distance_matrix(
    #         #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
    #         #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('waypoint2_point_latitude'), validated_data.get('waypoint2_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
    #         # )

    #     d_point = Point(Decimal(validated_data.get('d_point_longitude')), Decimal(validated_data.get('d_point_latitude')), srid=4326)

    #     instance.amount=new_amount if new_amount != instance.new_amount else instance.new_amount
    #     # instance.driver=driver if instance.driver == None else instance.driver
    #     instance.p_point=p_point if p_point != instance.p_point else instance.p_point
    #     instance.d_point=d_point if d_point != instance.d_point else instance.d_point
    #     instance.waypoint1_point=w1_point if w1_point != instance.w1_point else instance.w1_point
    #     instance.waypoint2_point=w2_point if w2_point != instance.w2_point else instance.w2_point
    #     instance.car_type=car_type if car_type != instance.car_type else instance.car_type
    #     instance = Trips.objects.filter(uuid=instance.uuid).update(
    #         p_point=p_point,
    #         d_point=d_point,
    #         waypoint1_point=w1_point,
    #         waypoint2_point=w2_point,
    #         car_type=car_type,
    #         **validated_data
    #     )
    #     return instance
