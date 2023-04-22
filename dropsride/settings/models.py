import datetime
import uuid
from datetime import date
from decimal import Decimal

from countries_plus.models import Country
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    Avg,
    BooleanField,
    CharField,
    Count,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FloatField,
    ForeignKey,
    GenericIPAddressField,
    IntegerField,
    ManyToManyField,
    Max,
    OneToOneField,
    PositiveBigIntegerField,
    PositiveSmallIntegerField,
    Q,
    SlugField,
    Sum,
    TextField,
    TimeField,
    URLField,
    UUIDField,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from stdimage import StdImageField
from tinymce.models import HTMLField

from dropsride.currency.models import States

User = settings.AUTH_USER_MODEL


# Staff Required to create this by defaults
class Localization(TimeStampedModel):
    """For every state there shall be individual rates per km as well as rates
    to be taken from drivers per day

    Args:
        TimeStampedModel (AbstractModel): to represent Created(DateTimeField) and Modified(DateTimeField - Auto)
    """

    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    state = OneToOneField(
        States, on_delete=CASCADE, related_name="states", db_index=True
    )
    tiket_fare = DecimalField(
        _("Drivers Ticket Fee"),
        max_digits=20,
        decimal_places=2,
        default=3.22,
        db_index=True,
    )
    base_price = DecimalField(
        _("Base Fare"), max_digits=20, decimal_places=2, default=1.00
    )
    cost_per_km = DecimalField(
        _("Cost Per KM"), max_digits=20, decimal_places=2, default=0.60
    )
    cost_per_15min = DecimalField(
        _("Cost Per 15 Minutes"), max_digits=20, decimal_places=2, default=0.32
    )

    def __str__(self):
        return self.state.state.title()

    def get_absolute_url(self):
        return reverse("settings:localization_detail", kwargs={"uuid": self.uuid})

    class Meta:
        managed = True
        verbose_name = "Localization"
        verbose_name_plural = "Localizations"
        ordering = ["state__country_iso", "state__state"]


# Staff Required to create this by defaults
class CarType(TimeStampedModel):
    """For each type of car add the amount to the total cost per km of a given
    localization. Then if a trip is less than 1km add the base price for that state
    to the car type amount for the driver

    Args:
        TimeStampedModel (AbstractModel): to represent Created(DateTimeField) and Modified(DateTimeField - Auto)
    """

    image = StdImageField(
        _("Car Photo"),
        upload_to="car/cover",
        blank=True,
        delete_orphans=True,
        variations={"thumbnail": {"width": 100, "height": 100, "crop": True}},
    )
    title = CharField(
        _("Car Type Name"),
        max_length=20,
        blank=True,
        help_text="Lite, Premium, Royalty, Shared",
    )
    slug = SlugField(_("Slug"), blank=True, max_length=500, db_index=True, unique=True)
    amount = DecimalField(
        _("Fixed Maintenance Fee"), max_digits=20, decimal_places=2, default=0.00
    )
    seats = IntegerField(default=4)

    @property
    def drivers(self):
        if self.vehicle_type:
            return self.vehicle_type.filter(active=True)
        return None

    def __str__(self):
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Car Type"
        verbose_name_plural = "Car Types"
        ordering = ["-modified", "title"]

    def get_absolute_url(self):
        return reverse("settings:cartype_detail", kwargs={"slug": self.slug})
