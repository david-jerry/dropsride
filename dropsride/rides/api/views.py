from datetime import date, datetime, timedelta
from decimal import Decimal

import googlemaps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Q
from django.utils import timezone
from humanfriendly import format_length, format_timespan
from rest_framework import status
# from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from dropsride.rides.api.serializers import RatingSerializer, TripsSerializer
from dropsride.rides.models import Rating, Trips
from dropsride.settings.models import CarType, Localization
from dropsride.tickets.models import TicketSubscription
from dropsride.utils.logger import LOGGER

User = get_user_model()
gmaps = googlemaps.Client(key=settings.GOOGLE_API)


class RatingViewset(
    RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet
):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    lookup_field = "pk"
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class TripsViewset(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = TripsSerializer
    queryset = Trips.objects.all()
    lookup_field = "uuid"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    # def get_queryset(self, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         return self.queryset
    #     elif self.request.user.is_driver:
    #         return self.queryset.filter(driver__username=self.request.user.username)
    #     elif not self.request.user.is_driver and not self.request.user.is_staff:
    #         return self.queryset.filter(user__username=self.request.user.username)

    def create(self, request, *args, **kwargs):
        validated_data = request.data
        localization = Localization.objects.get(
            state__state=validated_data.get("state")
        )
        state = validated_data.get("state")
        p_point = Point(
            float(validated_data.get("p_point_longitude")),
            float(validated_data.get("p_point_latitude")),
            srid=4326,
        )
        w1_point = Point(0.00, 0.00, srid=4326)
        w2_point = Point(0.00, 0.00, srid=4326)
        LOGGER.info(validated_data.get("pickup"))
        origin = validated_data.get("pickup")
        destination = validated_data.get("dropoff")
        if validated_data.get("waypoint1_point_longitude") and not validated_data.get(
            "waypoint2_point_longitude"
        ):
            w1_point = Point(
                float(validated_data.get("waypoint1_point_longitude")),
                float(validated_data.get("waypoint1_point_latitude")),
                srid=4326,
            )
            pdistances = gmaps.distance_matrix(
                validated_data.get("pickup"), validated_data.get("waypoint1_address")
            )["rows"][0]["elements"][0]
            distances = gmaps.distance_matrix(
                validated_data.get("waypoint1_address"), validated_data.get("dropoff")
            )["rows"][0]["elements"][0]
            distance_km = (
                Decimal(pdistances["distance"]["value"])
                + Decimal(distances["distance"]["value"])
            ) / Decimal(1000.00)
            duration_s = Decimal(pdistances["duration"]["value"]) + Decimal(
                distances["duration"]["value"]
            )

            # res = gmaps.distance_matrix(
            #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
            #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
            # )
        elif validated_data.get("waypoint2_point_longitude"):
            w2_point = Point(
                float(validated_data.get("waypoint2_point_longitude")),
                float(validated_data.get("waypoint2_point_latitude")),
                srid=4326,
            )
            w1_point = Point(
                float(validated_data.get("waypoint1_point_longitude")),
                float(validated_data.get("waypoint1_point_latitude")),
                srid=4326,
            )
            pdistances = gmaps.distance_matrix(
                validated_data.get("pickup"), validated_data.get("waypoint1_address")
            )["rows"][0]["elements"][0]
            wdistances = gmaps.distance_matrix(
                validated_data.get("waypoint1_address"),
                validated_data.get("waypoint2_address"),
            )["rows"][0]["elements"][0]
            distances = gmaps.distance_matrix(
                validated_data.get("waypoint2_address"), validated_data.get("dropoff")
            )["rows"][0]["elements"][0]
            distance_km = (
                Decimal(pdistances["distance"]["value"])
                + Decimal(wdistances["distance"]["value"])
                + Decimal(distances["distance"]["value"])
            ) / Decimal(1000.00)
            duration_s = (
                Decimal(pdistances["duration"]["value"])
                + Decimal(wdistances["duration"]["value"])
                + Decimal(distances["duration"]["value"])
            )

            # res = gmaps.distance_matrix(
            #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
            #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('waypoint2_point_latitude'), validated_data.get('waypoint2_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
            # )
        else:
            pdistances = gmaps.distance_matrix(origin, destination)["rows"][0][
                "elements"
            ][0]
            LOGGER.info(gmaps.distance_matrix(origin, destination))
            distance_km = Decimal(pdistances["distance"]["value"]) / Decimal(1000.00)
            duration_s = Decimal(pdistances["duration"]["value"])

        d_point = Point(
            float(validated_data.get("d_point_longitude")),
            float(validated_data.get("d_point_latitude")),
            srid=4326,
        )

        arrival_time = timezone.now() + timedelta(seconds=int(duration_s))
        fmt_sec = format_timespan(duration_s)
        fmt_dist = format_length(distance_km)
        amount = Decimal(distance_km) * Decimal(localization.cost_per_km)

        user = request.user
        user.on_a_ride = True
        user.save()
        trip = Trips.objects.create(
            user=user,
            amount=amount,
            fmt_sec=fmt_sec,
            fmt_dist=fmt_dist,
            p_point=p_point,
            d_point=d_point,
            waypoint1_point=w1_point,
            waypoint2_point=w2_point,
            distance_km=distance_km,
            arrival_time=arrival_time,
            state=state,
        )
        # if w1_point != "" or w2_point != "":
        # else:
        #     trip = Trips.objects.create(user=user, amount=amount, fmt_sec=fmt_sec, fmt_dist=fmt_dist, p_point=p_point, d_point=d_point, distance_km=distance_km, arrival_time=arrival_time, state=state)
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "data": serializer.data,
                "message": f"Choose A Car Type and Complete booking",
                "uid": trip.uuid,
                "assigned": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def assign(self, request, *args, **kwargs):
        instance = self.get_object()
        cordinates = instance.p_point
        car_type = CarType.objects.get(id=int(request.data.get("car_type")))
        # drivers = TicketSubscription.objects.filter(status=TicketSubscription.ACTIVE, driver__is_active=True, driver__userState=user.userState, driver__is_driver=True, driver__on_a_ride=False, driver__location__distance_lt=(user.location, Distance(m=2000)))[:30]
        drivers = TicketSubscription.objects.filter(
            status=TicketSubscription.ACTIVE,
            driver__is_active=True,
            driver__userState=request.user.userState,
            driver__is_driver=True,
            driver__on_a_ride=False,
            driver__location__distance_lt=(instance.user.location, Distance(m=10000)),
        )[:10]
        LOGGER.info(drivers)
        if len(drivers) > 0:
            ticket = drivers.first()
            validated_data = request.data
            localization = Localization.objects.get(state__state=instance.state)
            state = instance.state
            p_point = instance.p_point
            w1_point = Point(0.00, 0.00, srid=4326)
            w2_point = Point(0.00, 0.00, srid=4326)
            LOGGER.info(validated_data.get("pickup"))
            origin = validated_data.get("pickup")
            destination = validated_data.get("dropoff")
            if validated_data.get(
                "waypoint1_point_longitude"
            ) and not validated_data.get("waypoint2_point_longitude"):
                w1_point = Point(
                    float(validated_data.get("waypoint1_point_longitude")),
                    float(validated_data.get("waypoint1_point_latitude")),
                    srid=4326,
                )
                pdistances = gmaps.distance_matrix(
                    validated_data.get("pickup"),
                    validated_data.get("waypoint1_address"),
                )["rows"][0]["elements"][0]
                distances = gmaps.distance_matrix(
                    validated_data.get("waypoint1_address"),
                    validated_data.get("dropoff"),
                )["rows"][0]["elements"][0]
                distance_km = (
                    Decimal(pdistances["distance"]["value"])
                    + Decimal(distances["distance"]["value"])
                ) / Decimal(1000.00)
                duration_s = Decimal(pdistances["duration"]["value"]) + Decimal(
                    distances["duration"]["value"]
                )

                # res = gmaps.distance_matrix(
                #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
                #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
                # )
            elif validated_data.get("waypoint2_point_longitude"):
                w2_point = Point(
                    float(validated_data.get("waypoint2_point_longitude")),
                    float(validated_data.get("waypoint2_point_latitude")),
                    srid=4326,
                )
                w1_point = Point(
                    float(validated_data.get("waypoint1_point_longitude")),
                    float(validated_data.get("waypoint1_point_latitude")),
                    srid=4326,
                )
                pdistances = gmaps.distance_matrix(
                    validated_data.get("pickup"),
                    validated_data.get("waypoint1_address"),
                )["rows"][0]["elements"][0]
                wdistances = gmaps.distance_matrix(
                    validated_data.get("waypoint1_address"),
                    validated_data.get("waypoint2_address"),
                )["rows"][0]["elements"][0]
                distances = gmaps.distance_matrix(
                    validated_data.get("waypoint2_address"),
                    validated_data.get("dropoff"),
                )["rows"][0]["elements"][0]
                distance_km = (
                    Decimal(pdistances["distance"]["value"])
                    + Decimal(wdistances["distance"]["value"])
                    + Decimal(distances["distance"]["value"])
                ) / Decimal(1000.00)
                duration_s = (
                    Decimal(pdistances["duration"]["value"])
                    + Decimal(wdistances["duration"]["value"])
                    + Decimal(distances["duration"]["value"])
                )

                # res = gmaps.distance_matrix(
                #     origin = [(validated_data.get('p_point_latitude'), validated_data.get('p_point_longitude'))],
                #     destinations = [(validated_data.get('waypoint1_point_latitude'), validated_data.get('waypoint1_point_longitude')), (validated_data.get('waypoint2_point_latitude'), validated_data.get('waypoint2_point_longitude')), (validated_data.get('d_point_latitude'), validated_data.get('d_point_longitude'))]
                # )
            else:
                pdistances = gmaps.distance_matrix(origin, destination)["rows"][0][
                    "elements"
                ][0]
                LOGGER.info(gmaps.distance_matrix(origin, destination))
                distance_km = Decimal(pdistances["distance"]["value"]) / Decimal(
                    1000.00
                )
                duration_s = Decimal(pdistances["duration"]["value"])

            d_point = instance.d_point

            arrival_time = timezone.now() + timedelta(seconds=int(duration_s))
            LOGGER.info(arrival_time)
            LOGGER.info(datetime.now())
            fmt_sec = format_timespan(duration_s)
            fmt_dist = format_length(distance_km)
            amount = (
                Decimal(distance_km) * Decimal(localization.cost_per_km)
                + car_type.amount
            )

            user = request.user
            # trip = Trips.objects.create(user=user, amount=amount, fmt_sec=fmt_sec, fmt_dist=fmt_dist, p_point=p_point, d_point=d_point, waypoint1_point=w1_point, waypoint2_point=w2_point, distance_km=distance_km, arrival_time=arrival_time, state=state)
            trip = Trips.objects.filter(uuid=instance.uuid).update(
                amount=amount,
                fmt_sec=fmt_sec,
                fmt_dist=fmt_dist,
                p_point=p_point,
                active=True,
                d_point=d_point,
                waypoint1_point=w1_point,
                waypoint2_point=w2_point,
                status=Trips.SELECTEDDRIVER,
                distance_km=distance_km,
                arrival_time=arrival_time,
                state=state,
                car_type=car_type,
            )

            # Trips.objects.filter(uuid=instance.uuid).update(amount=new_amount, driver=driver, car_type=car_type)
            serializer = TripsSerializer(trip, context={"request": request})
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "message": f"Driver Assigned",
                    "driver_username": ticket.driver.username,
                    "driver_lat": ticket.driver.latitude,
                    "driver_lng": ticket.driver.longitude,
                    "rider_username": instance.user.username,
                    "rider_lat": instance.user.latitude,
                    "rider_lng": instance.user.longitude,
                    "assigned": True,
                },
            )
        else:
            user = request.user
            instance.delete()
            return Response(
                data={
                    "message": f"No Driver currently within your location",
                    "driver_username": None,
                    "rider_username": instance.user.username,
                    "rider_lat": instance.user.latitude,
                    "rider_lng": instance.user.longitude,
                    "assigned": False,
                }
            )

    @action(
        detail=True, methods=["get"], permission_classes=[IsAuthenticatedOrReadOnly]
    )
    def reassignnewdriver(self, request, *args, **kwargs):
        instance = self.get_object()
        old_driver = instance.driver
        drivers = TicketSubscription.objects.filter(
            status=TicketSubscription.ACTIVE,
            driver__is_active=True,
            driver__userState=request.user.userState,
            driver__is_driver=True,
            driver__on_a_ride=False,
            driver__location__distance_lt=(instance.user.location, Distance(m=10000)),
        ).exclude(driver=old_driver)[:10]
        if drivers is not None:
            ticket = drivers.first()
            trip = Trips.objects.filter(uuid=instance.uuid).update(driver=ticket.driver)
            serializer = TripsSerializer(trip, context={"request": request})
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "message": f"Driver Assigned",
                    "driver_id": ticket.driver.id,
                    "driver_lat": ticket.driver.latitude,
                    "driver_lng": ticket.driver.longitude,
                    "assigned": True,
                },
            )
        else:
            car_type = CarType.objects.get(id=int(request.data.get("car_type")))
            new_amount = instance.amount + car_type.amount
            trip = Trips.objects.filter(uuid=instance.uuid).update(
                amount=new_amount, car_type=car_type
            )
            serializer = TripsSerializer(trip, context={"request": request})
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "message": f"No Driver currently within your location",
                    "driver_id": 0,
                    "assigned": False,
                },
            )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def accepttrip(self, request, *args, **kwargs):
        user = request.user
        trip = self.get_object()
        User.objects.filter(username=trip.driver.username).update(on_a_ride=True)
        if trip.driver is user and trip.status == Trips.SEARCHING:
            trip.status = Trips.ACCEPTED
            trip.driver.on_a_ride = True
            trip.driver.save(update_fields=["on_a_ride"])
            trip.save(update_fields=["status"])
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": f"You accepted a ride",
                "declined": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def driverarrivedpickup(self, request, *args, **kwargs):
        user = request.user
        trip = self.get_object()
        if trip.driver is user and trip.status == Trips.ACCEPTED:
            trip.driver_arrived = datetime.now()
            trip.status = Trips.ARRIVED
            trip.save(update_fields=["driver_arrived", "status"])
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": f"Driver arrived your location",
                "declined": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def driver_started_ride(self, request, *args, **kwargs):
        user = request.user
        trip = self.get_object()
        if trip.driver is user and trip.status == Trips.ARRIVED:
            trip.depature_time = datetime.now()
            trip.status = Trips.RIDESTARTED
            trip.save(update_fields=["depature_time", "status"])
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": f"Driver has started the ride",
                "declined": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def enroutestatus(self, request, *args, **kwargs):
        user = request.user
        trip = self.get_object()
        if trip.driver is user and trip.status == Trips.RIDESTARTED:
            trip.status = Trips.ONGOING
            trip.save(update_fields=["status"])
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": f"Driver is heading to your destination",
                "declined": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def driverendride(self, request, *args, **kwargs):
        user = request.user
        trip = self.get_object()
        trip.user.on_a_ride = False
        trip.driver.on_a_ride = False
        trip.user.save()
        trip.driver.save()
        if trip.driver is user and trip.status == Trips.ONGOING:
            trip.arrival_time = datetime.now()
            trip.status = Trips.COMPLETED
            trip.active = False
            trip.save(update_fields=["arrival_time", "status"])
        serializer = TripsSerializer(trip, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": f"Driver arrived your destination and ended the ride",
                "declined": False,
            },
        )

    @action(
        detail=True,
        methods=["get", "post", "put"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def declinetrip(self, request, *args, **kwargs):
        instance = self.get_object()
        cordinates = instance.p_point
        drivers = TicketSubscription.objects.filter(
            status=TicketSubscription.ACTIVE,
            driver__is_active=True,
            driver__userState=instance.user.userState,
            driver__is_driver=True,
            driver__on_a_ride=False,
            driver__location__distance_lt=(cordinates, Distance(m=5000)),
        ).exclude(driver=instance.driver)[:10]
        if drivers:
            driver = drivers.first()
            Trips.objects.filter(uuid=instance.uuid).update(driver=driver)
            serializer = TripsSerializer(instance, context={"request": request})
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "message": f"You declined a ride",
                    "declined": True,
                },
            )
        else:
            instance.user.on_a_ride = False
            instance.driver.on_a_ride = False
            instance.user.save()
            instance.driver.save()
            instance.delete()
            return Response(
                status=status.HTTP_400_NOT_FOUND,
                data={"message": "No available driver at the moment"},
            )

    @action(
        detail=True,
        methods=["get", "post", "delete"],
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def cancletrip(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        if (
            instance.rider.username == user.username
            or instance.driver.username == user.username
        ):
            instance.user.on_a_ride = False
            instance.driver.on_a_ride = False
            instance.user.save()
            instance.driver.save()
            instance.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={"message": f"You canclled a ride", "cancelled": True},
        )
