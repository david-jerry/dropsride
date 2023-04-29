import uuid
from datetime import date, timedelta

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    OneToOneField,
    PositiveIntegerField,
    UUIDField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from dropsride.settings.models import Localization
from dropsride.transactions.models import Transaction
from dropsride.utils.logger import LOGGER

User = settings.AUTH_USER_MODEL
today = date.today()


# Create your models here.
class TicketPlans(TimeStampedModel):
    """
    This is the approved plans for ticketing by drops ride with its defined payment costs.
    """

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUATERLY = "quaterly"
    ANNUALLY = "annually"
    CHOICES = (
        (DAILY, DAILY),
        (WEEKLY, WEEKLY),
        (MONTHLY, MONTHLY),
        (QUATERLY, QUATERLY),
        (ANNUALLY, ANNUALLY),
    )

    DAY = 1
    WEEK = 7
    MONTH = 30
    QUATER = 120
    YEAR = 365
    DURATION = (
        (DAY, "DAY"),
        (WEEK, "WEEK"),
        (MONTH, "MONTH"),
        (QUATER, "QUATER"),
        (YEAR, "YEAR"),
    )

    interval = CharField(
        _("Plan Duration"), max_length=25, blank=True, choices=CHOICES, default=DAILY
    )
    duration = PositiveIntegerField(_("Duration"), choices=DURATION, default=DAY)
    localization = OneToOneField(
        Localization, on_delete=CASCADE, related_name="localization", db_index=True
    )

    @property
    def amount(self):
        return self.localization.tiket_fare

    @property
    def pay_amount(self):
        return int(round(self.localization.tiket_fare))

    @property
    def state(self):
        return self.localization.state.state

    @property
    def title(self):
        return f"{self.localization.state} Drivers Ticket Plan"

    def __str__(self):
        return f"{self.localization.state} Drivers Ticket Plan"

    def get_absolute_url(self):
        return reverse("tickets:plan", kwargs={"pk": self.pk})

    class Meta:
        managed = True
        verbose_name = "Ticket Plan"
        verbose_name_plural = "Ticket Plans"
        ordering = ["-modified"]


class TicketSubscription(TimeStampedModel):
    """Drivers subscribe to a plan. When they login the login receiver check if the driver's subscription plan is active and then changes the status where it is required

    Args:
        TimeStampedModel (_type_): _description_
    """

    ACTIVE = "active"
    EXPIRED = "expired"
    STATUS = ((ACTIVE, ACTIVE), (EXPIRED, EXPIRED))

    id = UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    driver = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="driver_subscription",
        blank=True,
        null=True,
        db_index=True,
    )

    status = CharField(
        _("Ticket Status"), max_length=15, choices=STATUS, default=EXPIRED
    )
    plan = ForeignKey(
        TicketPlans,
        on_delete=CASCADE,
        related_name="plan",
        null=True,
        blank=True,
        db_index=True,
    )
    expiry_date = DateField(blank=True, null=True)

    transaction = GenericRelation(Transaction, blank=True, null=True)
    active = BooleanField(default=False)

    @property
    def ticket_amount(self):
        if self.plan is not None and self.driver.wallet.currency.code != "USD":
            return (
                self.plan.pay_amount * int(round(self.driver.wallet.currency.price))
            ) * 100
        return self.plan.pay_amount * 100

    def get_queryset(self):
        return self.__class__.objects.filter(user=self.user)

    def deactivate_ticket(self):
        if self.active and date.today() > self.expiry_date:
            obj = self.get_queryset().select_for_update().get()
            obj.status = TicketSubscription.EXPIRED
            obj.active = False
            obj.save(update_fields=["status", "active"])

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = "Ticket Subscription"
        verbose_name_plural = "Tickets Subscription"
        ordering = ["-modified"]
