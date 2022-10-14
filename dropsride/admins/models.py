from datetime import date

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

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country

from dropsride.users.models import User

class Admins(TimeStampedModel):
    user = OneToOneField(User,
        on_delete=CASCADE,
        related_name="admin",
        verbose_name=_("Admin"),
        help_text=_("Admins on Dropsride"),
    )

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
        ordering = ["-created"]

