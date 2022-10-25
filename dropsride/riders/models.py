from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    FloatField,
    DateField,
    DecimalField,
    URLField,
    TextField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from dropsride.riders.managers import RidersManager

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

from dropsride.users.models import User

class Riders(TimeStampedModel):
    user = OneToOneField(User,
        on_delete=CASCADE,
        related_name="rider",
        verbose_name=_("Rider"),
        help_text=_("Riders on Dropsride"),
    )

    approved = BooleanField(default=True)
    objects = RidersManager()

    def get_absolute_url(self):
        return reverse("riders:detail", kwargs={"id": self.id})

    def get_next(self):
        next = self.__class__.objects.filter(approved=True, created__gt=self.created).order_by("user__id")
        try:
            return next[0]
        except IndexError:
            return None

    def get_prev(self):
        prev = self.__class__.objects.filter(approved=True, created__lt=self.created).order_by("user__id")
        try:
            return prev[0]
        except IndexError:
            return None



    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        verbose_name = "Rider"
        verbose_name_plural = "Riders"
        ordering = ["-created"]


class RiderSavedAddress(TimeStampedModel):
    """Addresses for every rider to be quick picked

    Args:
        TimeStampedModel (_type_): _description_
    """

    HOME = "HOME"
    OFFICE = "OFFICE"
    SCHOOL = "SCHOOL"
    CHURCH = "CHURCH"
    ADDRESS_TYPE=(
        (HOME, HOME),
        (OFFICE, OFFICE),
        (SCHOOL, SCHOOL),
        (CHURCH, CHURCH)
    )

    rider = ForeignKey(Riders, on_delete=CASCADE, related_name="rider_address")

    address_type = CharField(max_length=500, choices=ADDRESS_TYPE, default=HOME, unique=True)

    address = CharField(max_length=500, blank=True, null=True)
    city = CharField(max_length=500, blank=True, null=True)
    post_code = CharField(max_length=500, blank=True, null=True)
    state = CharField(max_length=500, blank=True, null=True)
    country = CharField(max_length=500, blank=True, null=True)
    latitude = CharField(max_length=500, blank=True, null=True)
    longitude = CharField(max_length=500, blank=True, null=True)

    captcha_score = FloatField(default=0.00)

    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.rider.user.username.upper()} {self.address_type}"

    class Meta:
        managed = True
        verbose_name = "Rider Address"
        verbose_name_plural = "Riders Addresses"
        ordering = ["-created"]


class RiderWallet(TimeStampedModel):
    """Wallet to store riders deposited funds for rides.

    Args:
        TimeStampedModel (_type_): _description_
    """
    rider = OneToOneField(Riders, on_delete=CASCADE, related_name="rider_wallet")
    balance = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    unlocked = BooleanField(default=False)

    def __str__(self):
        return f"{self.rider.user.username.upper()} {self.balance}"

    class Meta:
        managed = True
        verbose_name = "Rider Wallet"
        verbose_name_plural = "Riders Wallet"
        ordering = ["-created"]


class RiderTransactionHistory(TimeStampedModel):
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

    rider = ForeignKey(Riders, on_delete=CASCADE, related_name="rider_transactions")
    amount = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    transaction_id = CharField(max_length=50, blank=True)
    status = CharField(max_length=25, choices=TRANSACTION_STATUS, default=PENDING)

    def __str__(self):
        return f"{self.rider.user.username.upper()} {self.transaction_id}"

    class Meta:
        managed = True
        verbose_name = "Rider Transaction History"
        verbose_name_plural = "Riders Transaction Histories"
        ordering = ["-created"]

