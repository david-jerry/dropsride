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

from model_utils.models import TimeStampedModel

# Create your models here.
class Coupons(TimeStampedModel):
    """Create coupons for users and other promotions for special days

    Args:
        TimeStampedModel (_type_): _description_
    """

    code = CharField(max_length=8, unique=True)
    discount = DecimalField(decimal_places=2, max_digits=8, default=0.00)
    valid_from = DateField()
    valid_to = DateField()

    active = BooleanField(default=False)

    def __str__(self):
        return self.code


