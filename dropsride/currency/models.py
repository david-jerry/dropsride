from django.db.models import CharField, DecimalField, SlugField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class States(TimeStampedModel):
    """Supported states available

    Args:
        TimeStampedModel (AbstractModel): to represent Created(DateTimeField) and Modified(DateTimeField - Auto)

    Returns:
        String: Names of states covered in the localization model under trips
    """

    state = CharField(max_length=500, unique=True, db_index=True)
    country_iso = CharField(max_length=4)

    def __str__(self):
        return self.state


class Banks(TimeStampedModel):
    """Supported banks from paystack

    Args:
        TimeStampedModel (AbstractModel): to represent Created(DateTimeField) and Modified(DateTimeField - Auto)
    """

    name = CharField(max_length=500, unique=True)
    slug = SlugField(unique=True)
    lcode = CharField(max_length=25, db_index=True)
    code = CharField(max_length=10, db_index=True)
    country_iso = CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")
        ordering = ["name"]


class Currency(TimeStampedModel):
    """
    Supported Currencies for exchange rates to user desired currency
    all converted to a unified base Unit (USD)
    """

    NGN = "NGN"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    CNY = "CNY"
    JPY = "JPY"
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    DKK = "DKK"
    SEK = "SEK"
    ZAR = "ZAR"
    AED = "AED"
    CODE = (
        (NGN, "Nigerian Naira"),
        (USD, "United States Dollar"),
        (EUR, "Euro"),
        (GBP, "British Pound"),
        (CNY, "Chinese Yuan"),
        (JPY, "Japanese Yen"),
        (AUD, "Australian Dollar"),
        (CAD, "Canadian Dollar"),
        (CHF, "Swiss Franc"),
        (DKK, "Danish Krone"),
        (SEK, "Swedish Krona"),
        (ZAR, "South African Rand"),
        (AED, "United Arab Emirates Dirham"),
    )
    code = CharField(
        max_length=3,
        choices=CODE,
        default=USD,
        blank=False,
        null=False,
        unique=True,
        db_index=True,
    )
    symbol = CharField(max_length=10, blank=False, null=False, unique=False)
    price = DecimalField(
        max_digits=20, decimal_places=2, blank=False, default=0.00, null=False
    )

    def __str__(self):
        return f"{self.code} - {self.symbol.upper()} {round(self.price, 2)}"

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["code"]
