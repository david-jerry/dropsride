from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.templatetags.static import static

from webpush import send_user_notification, send_group_notification

from dropsride.utils.logger import LOGGER
from .models import DriverWallet, Drivers

@receiver(post_save, sender=Drivers)
def unlock_wallet(instance, created, **kwargs):
    if not DriverWallet.objects.filter(driver=instance).exists():
        DriverWallet.objects.create(driver=instance)
        LOGGER.info("[DRIVER] Creating wallet relationshio")

@receiver(post_save, sender=DriverWallet)
def unlock_wallet(instance, created, **kwargs):
    if instance.balance >= Decimal(1000) and instance.unlocked == False:
        DriverWallet.objects.filter(driver=instance.driver).update(unlocked=True)

        link = f"/users/{instance.driver.user.username}/"
        domain = "https://www.dropsride.com" if settings.PRODUCTION else "localhost:8000"
        payload = {
            'head': "DRIVER WALLET",
            'body': f"Your wallet has been unlocked.\n\n{domain}{link}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': f"{domain}{link}",
        }
        send_user_notification(user=instance.driver.user, payload=payload, ttl=1000)
        LOGGER.info("[DRIVER WALLET] Unlocking wallet")
