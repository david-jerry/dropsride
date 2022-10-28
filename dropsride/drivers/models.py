from datetime import date, timedelta, timezone

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    URLField,
    TextField,
    ForeignKey,
    FloatField,
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

from dropsride.drivers.managers import DriversManager
# from dropsride.sitesettings.models import VehicleType
from dropsride.users.models import User


class Drivers(TimeStampedModel):
    """Drivers app where they will be rated and flagged based on the ratings they earn
    should they go below 3.5 thwy will be warned and given 30 days to raise it else they automatically
    get blocked. This notification will be sent as a push notification to the drivers phone

    Every rid that ends without a review gets to be automatically marked as 3.5 rating.

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """

    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="driver",
        verbose_name=_("Driver"),
        help_text=_("Drivers on Dropsride"),
    )
    is_blocked = BooleanField(default=False)

    address = CharField(max_length=500, blank=True, null=True)
    city = CharField(max_length=500, blank=True, null=True)
    post_code = CharField(max_length=500, blank=True, null=True)
    state = CharField(max_length=500, blank=True, null=True)
    country = CharField(max_length=500, blank=True, null=True)
    latitude = CharField(max_length=500, blank=True, null=True)
    longitude = CharField(max_length=500, blank=True, null=True)

    captcha_score = FloatField(default=0.00)

    objects = DriversManager()

    def get_driver_documents(self):
        if self.drivers_licence.approved_documents():
            return self.drivers_licence.approved_documents()
        return None

    @property
    def approved(self):
        if len(self.drivers_licence.approved_documents()) >= 6:
            return True
        return False

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("drivers:detail", kwargs={"id": self.id})

    def get_next(self):
        next = self.__class__.objects.filter(
            is_blocked=False, approved=True, created__gt=self.created
        ).order_by("user__id")
        try:
            return next[0]
        except IndexError:
            return None

    def get_prev(self):
        prev = self.__class__.objects.filter(
            is_blocked=False, approved=True, created__lt=self.created
        ).order_by("user__id")
        try:
            return prev[0]
        except IndexError:
            return None

    def get_driver_transactions(self):
        if self.driver_transactions:
            return self.driver_transactions.all()
        return None

    class Meta:
        managed = True
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
        ordering = ["-created"]


class Subscription(TimeStampedModel):
    DAY = "DAILY"
    MONTH = "MONTHLY"
    QUARTERYEAR = "QUARTER YEAR"
    HALFYEAR = "HALF YEAR"
    YEAR = "YEAR"
    PLANS = (
        (DAY, DAY),
        (MONTH, MONTH),
        (QUARTERYEAR, QUARTERYEAR),
        (HALFYEAR, HALFYEAR),
        (YEAR, YEAR),
    )

    driver = OneToOneField(
        Drivers, on_delete=CASCADE, related_name="subscription_driver"
    )
    plan = CharField(max_length=20, choices=PLANS, default=DAY)
    code = CharField(max_length=255)
    vehicle_type = ForeignKey(
        'sitesettings.VehicleType', on_delete=CASCADE, related_name="subscription_vehicle_type"
    )

    active = BooleanField(default=False)

    @property
    def deactivated(self):
        if self.plan == self.DAY:
            end_date = self.created + timedelta(days=1)
        elif self.plan == self.MONTH:
            end_date = self.created + timedelta(months=1)
        elif self.plan == self.QUARTERYEAR:
            end_date = self.created + timedelta(months=3)
        elif self.plan == self.HALFYEAR:
            end_date = self.created + timedelta(months=6)
        elif self.plan == self.YEAR:
            end_date = self.created + timedelta(months=12)

        if timezone.now() >= end_date:
            self.active = False
            self.save()
            return True
        return False

    def __str__(self) -> str:
        return f"{self.driver.user.username.title()} {self.plan} Subscription"

    class Meta:
        managed = True
        verbose_name = "Driver Subscription"
        verbose_name_plural = "Drivers Subscriptions"
        ordering = ["-created", "active"]


class DriverWallet(TimeStampedModel):
    """Wallet to store riders deposited funds for rides.

    Args:
        TimeStampedModel (_type_): _description_
    """
    driver = OneToOneField(Drivers, on_delete=CASCADE, related_name="driver_wallet")
    balance = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    unlocked = BooleanField(default=False)

    def __str__(self):
        return f"{self.driver.user.username.upper()} {self.balance}"

    class Meta:
        managed = True
        verbose_name = "Driver Wallet"
        verbose_name_plural = "Drivers Wallet"
        ordering = ["-created"]


class DriverTransactionHistory(TimeStampedModel):
    """Transactional history for a specific rider for wallet

    Args:
        TimeStampedModel (_type_): _description_
    """

    SUCCESS = "SUCCESS"
    PENDING = "PENDING"
    FAILED = "FAILED"
    TRANSACTION_STATUS = (
        (SUCCESS, SUCCESS),
        (PENDING, PENDING),
        (FAILED, FAILED),
    )

    driver = ForeignKey(Drivers, on_delete=CASCADE, related_name="driver_transactions")
    amount = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    transaction_id = CharField(max_length=50, blank=True)
    status = CharField(max_length=25, choices=TRANSACTION_STATUS, default=PENDING)

    def __str__(self):
        return f"{self.driver.user.username.upper()} {self.transaction_id}"

    class Meta:
        managed = True
        verbose_name = "Driver Transaction History"
        verbose_name_plural = "Drivers Transaction Histories"
        ordering = ["-created"]

