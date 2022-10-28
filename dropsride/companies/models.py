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
    Sum
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

from dropsride.users.models import User
from dropsride.companies.managers import CompanyManager

class Company(TimeStampedModel):
    user = OneToOneField(User,
        on_delete=CASCADE,
        related_name="company",
        verbose_name=_("company"),
        help_text=_("Company Account on Dropsride"),
    )
    company_name = CharField(max_length=255, blank=True, null=True)

    approved = BooleanField(default=False)
    objects = CompanyManager()

    def get_addresses(self):
        if self.company_address:
            return self.company_address.all()
        return None

    def get_company_transactions(self):
        if self.company_transactions:
            return self.company_transactions.all()
        return None

    def get_absolute_url(self):
        return reverse("companies:detail", kwargs={"id": self.id})

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
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["-created"]


class CompanySavedAddress(TimeStampedModel):
    """Addresses for every company to be quick picked

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

    company = ForeignKey(Company, on_delete=CASCADE, related_name="company_address")

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
        verbose_name = "Companies Address"
        verbose_name_plural = "Companies Addresses"
        ordering = ["-created"]


class CompanyWallet(TimeStampedModel):
    """Wallet to store riders deposited funds for rides.

    Args:
        TimeStampedModel (_type_): _description_
    """
    company = OneToOneField(Company, on_delete=CASCADE, related_name="company_wallet")
    balance = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    unlocked = BooleanField(default=False)

    alert_when_low = DecimalField(decimal_places=2, max_digits=20, default=0.00)

    def __str__(self):
        return f"{self.company.user.username.upper()} {self.balance}"

    class Meta:
        managed = True
        verbose_name = "Company Wallet"
        verbose_name_plural = "Companys Wallet"
        ordering = ["-created"]


class CompanyTransactionHistory(TimeStampedModel):
    """Transactional history for a specific company's wallet

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

    company = ForeignKey(Company, on_delete=CASCADE, related_name="company_transactions")
    amount = DecimalField(decimal_places=2, max_digits=20, default=0.00)
    transaction_id = CharField(max_length=50, blank=True)
    status = CharField(max_length=25, choices=TRANSACTION_STATUS, default=PENDING)

    def __str__(self):
        return f"{self.company.user.username.upper()} {self.transaction_id}"

    class Meta:
        managed = True
        verbose_name = "Company Transaction History"
        verbose_name_plural = "Companys Transaction Histories"
        ordering = ["-created"]
