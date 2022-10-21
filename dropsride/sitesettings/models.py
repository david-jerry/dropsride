from datetime import timezone, timedelta
from email.policy import default
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    EmailField,
    URLField,
    IntegerField,
    PositiveSmallIntegerField,
    TextField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum,
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

from dropsride.users.models import User
from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
# from dropsride.sitesettings.models import Localization


class SiteSettings(TimeStampedModel):
    """Setup site settings for dropsride

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    logo = StdImageField(
        _("Logo"),
        upload_to="settings/logo",
        blank=True,
        delete_orphans=True,
        variations={"thumbnail": {"width": 100, "height": 100, "crop": True}},
    )
    favicon = StdImageField(
        _("Favicon"),
        upload_to="settings/logo",
        blank=True,
        delete_orphans=True,
        variations={"thumbnail": {"width": 100, "height": 100, "crop": True}},
    )
    copyright = CharField(max_length=255)
    short_description = CharField(max_length=165)
    keywords = CharField(max_length=500)
    title = CharField(max_length=255)

    phone_number = CharField(max_length=255)
    phone_number_II = CharField(max_length=255)

    dispute_email = EmailField()
    contact_email = EmailField()

    playstore_link = URLField()
    applestore_link = URLField()

    enable_social_login = BooleanField(default=False)
    enable_wallet_savings = BooleanField(default=True)

    def __str__(self) -> str:
        return self.state.title()

    class Meta:
        managed = True
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
        ordering = ["-created"]


class SocialSiteSettings(TimeStampedModel):
    """Add social accounts for drops ride here

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    facebook = URLField()
    instagram = URLField()
    linkedin = URLField()
    twitter = URLField()
    pinterest = URLField()

    def __str__(self) -> str:
        return f"Social Accounts {self.id}"

    class Meta:
        managed = True
        verbose_name = "Site Social Account"
        verbose_name_plural = "Site Social Accounts"
        ordering = ["-created"]


class DriverSettings(TimeStampedModel):
    """Control the drivers search radius and waiting time from here

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    approved_waiting_time = IntegerField()
    driver_search_radius = IntegerField()

    def __str__(self) -> str:
        return f"Site Driver's Setting {self.id}"

    class Meta:
        managed = True
        verbose_name = "Site Drivers Setting"
        verbose_name_plural = "Site Drivers Settings"
        ordering = ["-created"]


class Localization(TimeStampedModel):
    """Set default subscription rate for drivers based off the location they are in

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    title = CharField(max_length=50, unique=True, blank=True, null=True)
    amount = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    rep = CharField(max_length=250, blank=True)
    head_office = CharField(max_length=500, blank=True)
    office_phone_1 = CharField(max_length=14, blank=True)
    office_phone_2 = CharField(max_length=14, blank=True)
    drivers = ManyToManyField(Drivers, blank=True)
    riders = ManyToManyField(Riders, blank=True)


    def __str__(self) -> str:
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Localization"
        verbose_name_plural = "Localization"
        ordering = ["-created"]


class VehicleType(TimeStampedModel):
    """This vehicle type controls everything about a vehicle.
    Covers the km_rate for the type of vehicle
    Covers the base rate for the vehicle
    Covers percentage increase for the type of vehicle based on the location


    with the parameters set we can determin the popularity of a vehicle by the amount of rides it has handled

    Args:
        TimeStampedModel (_type_): _description_
    """

    PRIVATE = "PRIVATE"
    BUSINESS = "BUSINESS"
    BUS = "BUS"
    MINIVAN = "MINIVAN"
    SHARED = "SHARED"
    VTYPE = (
        (PRIVATE, PRIVATE),
        (BUSINESS, BUSINESS),
        (BUS, BUS),
        (MINIVAN, MINIVAN),
        (SHARED, SHARED),
    )

    PENDING = "PENDING"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    VSTATUS = (
        (PENDING, PENDING),
        (ENABLED, ENABLED),
        (DISABLED, DISABLED),
    )

    v_type = CharField(max_length=50, unique=True, choices=VTYPE, default=PRIVATE)
    v_status = CharField(max_length=50, choices=VSTATUS, default=ENABLED)

    percentage = DecimalField(decimal_places=2, max_digits=6, default=0.00)
    default_rate_by_state = ForeignKey(
        Localization, on_delete=CASCADE, related_name="default_rate_by_location"
    )
    cost_per_km = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    base_unit = DecimalField(default=400.00, decimal_places=2, max_digits=20)

    max_seater = PositiveSmallIntegerField(default=4)
    max_luggage = PositiveSmallIntegerField(default=2)

    # drivers = ManyToManyField(Drivers, on_delete=CASCADE, related_name="no-of-drivers")
    # rides = ManyToManyField(Rides, on_delete=CASCADE, related_name="no-of-rides")

    @property
    def ticket_rate(self):
        _perc = self.default_rate_by_state.amount * self.percentage
        return self.default_rate_by_state.amount + _perc

    def __str__(self) -> str:
        return self.state.title()

    class Meta:
        managed = True
        verbose_name = "Vehicle Type"
        verbose_name_plural = "Vehicle Types"
        ordering = ["-created"]


class APIKeys(TimeStampedModel):
    google_api = CharField(max_length=500)
    google_captcha_key = CharField(max_length=500)
    google_captcha_secret_key = CharField(max_length=500)
    facebook_id = CharField(max_length=500)
    paystack_sk = CharField(max_length=500)
    paystack_pk = CharField(max_length=500)
    vapid_sk = CharField(max_length=500)
    vapid_pk = CharField(max_length=500)
    tinymce_sk = CharField(max_length=500)

    def __str__(self):
        return "Dropsride API Keys"


