from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.templatetags.static import static

from dropsride.utils.logger import LOGGER
from .models import RiderWallet, Riders

from webpush import send_user_notification, send_group_notification

@receiver(post_save, sender=Riders)
def create_wallet_with_rider_instance(instance, created, **kwargs):
    if not RiderWallet.objects.filter(rider=instance).exists():
        RiderWallet.objects.create(rider=instance)

@receiver(post_save, sender=RiderWallet)
def unlock_wallet(instance, created, **kwargs):
    if instance.balance >= Decimal(1000) and instance.unlocked == False:
        RiderWallet.objects.filter(rider=instance.rider).update(unlocked=True)

        link = f"/users/{instance.rider.user.username}/"
        domain = "https://www.dropsride.com" if settings.PRODUCTION else "localhost:8000"
        payload = {
            'head': "RIDER WALLET",
            'body': f"Your wallet has been unlocked.\n\n{domain}{link}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': f"{domain}{link}",
        }
        send_user_notification(user=instance.rider.user, payload=payload, ttl=1000)

