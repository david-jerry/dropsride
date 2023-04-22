import datetime
import uuid
from datetime import date
from decimal import Decimal

from countries_plus.models import Country
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.gis.geos import Point
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    Avg,
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    FloatField,
    ForeignKey,
    IntegerField,
    UUIDField,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from stdimage import StdImageField
from tinymce.models import HTMLField

from dropsride.settings.models import CarType
from dropsride.tickets.models import TicketSubscription
from dropsride.transactions.models import Transaction

User = settings.AUTH_USER_MODEL


# Staff Required to create this by defaults


class Trips(TimeStampedModel):
    """The trip is divided into two, shared or single rides. shared rides allows
    the driver to accept any ride heading towards the same destination.
    The riders gets to input the amount of passengers they are coming with to validate
    against the amount of seats a cartype has and what is left.
    Only riders who select shared rides are allowed to have a negligable discount.

    while single rides just encapsulates the total cost for the entire trip for a single rider.

    Args:
        TimeStampedModel (AbstractModel): to represent Created(DateTimeField) and Modified(DateTimeField - Auto)
    """

    # SHARED = "SHARED RIDE"
    # SINGLE = "SINGLE RIDE"
    # TRIP_TYPE = ((SHARED, SHARED), (SINGLE, SINGLE))
    # trip_type = CharField(
    #     _("Trip Type"), max_length=15, choices=TRIP_TYPE, default=SINGLE
    # )

    ACCEPTED = "ACCEPTED RIDE"
    ARRIVING = "ARRIVING PICKUP POINT"
    SELECTEDDRIVER = "SELECTED DRIVER WAITING CONFIRMATION"
    SEARCHING = "SEARCHING FOR DRIVER"
    PICKUPDES = "AT PICKUP DESTINATION"
    ARRIVED = "ARRIVED PICKUP POINT"
    RIDESTARTED = "STARTED RIDE"
    COMPLETED = "COMPLETED TRIP"
    ONGOING = "ONGOING TRANSIT"
    CANCELLED = "CANCELLED TRIP"
    PAUSED = "PAUSED TRIP"
    TRIP_STATUS = (
        (ACCEPTED, ACCEPTED),
        (ARRIVED, ARRIVED),
        (PICKUPDES, PICKUPDES),
        (SEARCHING, SEARCHING),
        (ARRIVING, ARRIVING),
        (RIDESTARTED, RIDESTARTED),
        (ONGOING, ONGOING),
        (COMPLETED, COMPLETED),
        (PAUSED, PAUSED),
        (CANCELLED, CANCELLED),
    )

    CARD = "CARD"
    CASH = "CASH"
    WALLET = "WALLET"
    PAY_METHOD = ((CARD, CARD), (CASH, CASH), (WALLET, WALLET))

    user = ForeignKey(
        User, on_delete=CASCADE, related_name="rider_trip", blank=True, null=True
    )
    driver = ForeignKey(
        User, on_delete=CASCADE, related_name="trip_driver", blank=True, null=True
    )

    state = CharField(max_length=50, blank=True, null=True)

    pickup = CharField(max_length=500, blank=True)
    p_longitude = FloatField(default=0.00)
    p_latitude = FloatField(default=0.00)
    dropoff = CharField(max_length=500, blank=True)
    d_longitude = FloatField(default=0.00)
    d_latitude = FloatField(default=0.00)

    distance_km = IntegerField(default=0)
    amount = DecimalField(max_digits=20, decimal_places=2, default=0.00)
    gross_total = DecimalField(max_digits=20, decimal_places=2, default=0.00)

    pay_method = CharField(
        _("Payment Method"), max_length=50, choices=PAY_METHOD, default=CASH
    )

    driver_arrived = DateTimeField(blank=True, null=True)
    depature_time = DateTimeField(blank=True, null=True)
    arrival_time = DateTimeField(blank=True, null=True)
    arrived_at = DateTimeField(blank=True, null=True)
    waiting_time = IntegerField(default=0)

    fmt_sec = CharField(max_length=50, blank=True, null=True)
    fmt_dist = CharField(max_length=50, blank=True, null=True)

    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    car_type = ForeignKey(
        CarType, on_delete=DO_NOTHING, related_name="car_type", blank=True, null=True
    )

    waypoint1_address = CharField(max_length=500, blank=True)
    waypoint1_longitude = FloatField(default=0.00)
    waypoint1_latitude = FloatField(default=0.00)

    waypoint2_address = CharField(max_length=500, blank=True)
    waypoint2_longitude = FloatField(default=0.00)
    waypoint2_latitude = FloatField(default=0.00)

    transaction = GenericRelation(Transaction)

    status = CharField(max_length=150, blank=False, default=SEARCHING)

    active = BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("rides:trip_detail", kwargs={"uuid": self.uuid})

    @property
    def average_rating(self) -> float:
        return (
            Rating.objects.filter(trip=self).aggregate(Avg("rating"))["rating__avg"]
            or 0
        )

    # @property
    # def closest_cars(self):
    #     cordinates = Point(self.p_point.x, self.p_point.y, srid=4326)
    #     drivers = TicketSubscription.objects.filter(status=TicketSubscription.ACTIVE, driver__is_active=True, driver__userState=self.state, driver__is_driver=True, driver__on_a_ride=False, driver__location__distance_lt=(cordinates, Distance(m=5000)))[:20]
    #     return

    # to create transactions just call the instance in a signal and do instance.transaction.create(**parameters)

    def __str__(self) -> str:
        return f"{self.uuid}: {self.average_rating}"

    class Meta:
        managed = True
        verbose_name = "Ride"
        verbose_name_plural = "Rides"
        ordering = ["-modified"]


class Rating(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="user")
    trip = ForeignKey(Trips, on_delete=CASCADE, related_name="trips")

    safety = IntegerField()
    comfort = IntegerField()
    fun = IntegerField()
    value_for_money = IntegerField()
    accessibility = IntegerField()
    wait_time = IntegerField()

    note = HTMLField()

    def __str__(self) -> str:
        return f"{self.trip.uuid}-{self.user.username}: {self.rating}"
