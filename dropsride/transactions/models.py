from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    CASCADE,
    CharField,
    DecimalField,
    ForeignKey,
    PositiveIntegerField,
    SlugField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

User = settings.AUTH_USER_MODEL


# Staff Required to create this by defaults
class Transaction(TimeStampedModel):
    """For every trip completed there should be a transaction history provided for the rider
    also for every ticket purchased there should be a transaction created and so on for profits made from
    a referral who joins the site newly. this model has a generic relationship to other models and can be used to
    store the relationship with them.

    Example:
        To create an instance to the model of choice with the relationship do this

        id = Model.objects.create(**data)
        id.transactions.create(owner=request.user, amount=amount_filled, transaction_reason=Transaction.DEPOSIT, transaction_status=Transaction.PAID)

        To get the counts and all transactions of a single model do this
        id.transactions.count()
        id.transactions.all()


    Args:
        TimeStampedModel (_type_): _description_
    """

    PAID = "PAID"
    OWEING = "OWEING"
    PENDING = "PENDING"
    FAILED = "FAILED"
    STATUS = ((PAID, PAID), (OWEING, OWEING), (PENDING, PENDING), (FAILED, FAILED))

    DEPOSIT = "WALLET DEPOSIT"
    CARD = "VERIFY DEBIT CARD"
    WITHDRAW = "WALLET WITHDRAWAL"
    PROFIT = "PROFIT EARNED"
    TRIP = "TRIP EARNED"
    TICKET = "TICKET PAYMENT"
    REASON = (
        (CARD, CARD),
        (DEPOSIT, DEPOSIT),
        (WITHDRAW, WITHDRAW),
        (PROFIT, PROFIT),
        (TRIP, TRIP),
        (TICKET, TICKET),
    )

    owner = ForeignKey(
        User, on_delete=CASCADE, related_name="user_transaction", db_index=True
    )

    slug = SlugField(max_length=700, null=True, blank=True, db_index=True)
    amount = DecimalField(max_digits=20, decimal_places=2, default=0.00)

    transaction_reason = CharField(
        _("Transaction Reason"), max_length=50, choices=REASON, default=DEPOSIT
    )
    transaction_status = CharField(
        _("Transaction Status"), max_length=15, choices=STATUS, default=PAID
    )

    ref_code = CharField(max_length=500, default="", blank=True, db_index=True)

    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"{self.transaction_reason}"

    def get_absolute_url(self):
        return reverse("transactions:details", kwargs={"slug": self.slug})

    class Meta:
        managed = True
        verbose_name = "Transactions"
        verbose_name_plural = "Transactions"
        ordering = ["-modified"]
