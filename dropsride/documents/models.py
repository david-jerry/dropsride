from datetime import date, timedelta, timezone
from enum import unique

from django.core.exceptions import ValidationError
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
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from dropsride.documents.managers import DocumentsManager

from dropsride.drivers.models import Drivers

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

# Create your models here.
class Documents(TimeStampedModel):
    """Submited Documents from a driver for verification

    Args:
        TimeStampedModel (_type_): _description_
    """

    DRVL_FRONT = "DRIVERS LICENCE F"
    DRVL_BACK = "DRIVERS LICENCE B"
    VEHICLE_OWNERSHIP = "PROOF OF OWNERSHIP"
    VEHICLE_LICENCE = "VEHICLE LICENCE"
    CHECK_CERT = "AUTOCHECK CERTIFICATE"
    INSURANCE = "INSURANCE"
    DOC_TYPE = (
        (DRVL_FRONT, DRVL_FRONT),
        (DRVL_BACK, DRVL_BACK),
        (VEHICLE_OWNERSHIP, VEHICLE_OWNERSHIP),
        (VEHICLE_LICENCE, VEHICLE_LICENCE),
        (CHECK_CERT, CHECK_CERT),
        (INSURANCE, INSURANCE),
    )

    document_type = CharField(max_length=150)
    driver = ForeignKey(Drivers, on_delete=CASCADE, related_name="drivers_licence")
    document = StdImageField()
    approved = BooleanField(default=False)

    objects = DocumentsManager()

    def __str__(self):
        return f"{self.driver.user.username.title()} Licence Documents"




