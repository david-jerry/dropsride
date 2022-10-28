from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.templatetags.static import static

from webpush import send_user_notification, send_group_notification

from dropsride.utils.logger import LOGGER
from .models import CompanyWallet, Company

@receiver(post_save, sender=Company)
def create_wallet_with_company_instance(instance, created, **kwargs):
    if not CompanyWallet.objects.filter(company=instance).exists():
        CompanyWallet.objects.create(company=instance)
        LOGGER.info("[COMPANY] Creating wallet relationshio")

@receiver(post_save, sender=CompanyWallet)
def unlock_wallet(instance, created, **kwargs):
    if instance.balance >= Decimal(1000) and instance.unlocked == False:
        CompanyWallet.objects.filter(company=instance.company).update(unlocked=True)
        link = f"/company/{instance.company.id}/"
        domain = "https://www.dropsride.com" if settings.PRODUCTION else "localhost:8000"
        payload = {
            'head': "COMPANY WALLET",
            'body': f"Your company account wallet has been unlocked.\n\n{domain}{link}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': f"{domain}{link}",
        }
        send_user_notification(user=instance.company.user, payload=payload, ttl=1000)

    if instance.balance <= instance.alert_when_low:
        link = f"/company/{instance.company.id}/"
        domain = "https://www.dropsride.com" if settings.PRODUCTION else "localhost:8000"
        payload = {
            'head': "COMPANY WALLET",
            'body': f"Your wallet balance is low.\nCurrent Balance: {instance.balance}.\n\n{domain}{link}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': f"{domain}{link}",
        }
        send_user_notification(user=instance.company.user, payload=payload, ttl=1000)
        LOGGER.info("[COMPANY WALLET] Unlocking wallet")
