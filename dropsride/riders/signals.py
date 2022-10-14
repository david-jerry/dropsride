from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives

from dropsride.utils.logger import LOGGER

from .models import RiderWallet


@receiver(post_save, sender=RiderWallet)
def unlock_wallet(instance, created, **kwargs):
    if instance.balance >= Decimal(1000) and instance.unlocked == False:
        instance.unlocked = True

