from datetime import date
from decimal import Decimal

from allauth.account.signals import user_logged_in, user_signed_up
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect
from django.templatetags.static import static
from notifications.signals import notify
from rest_framework.authtoken.models import Token
from webpush import send_group_notification, send_user_notification

from dropsride.core.tasks import send_html_email
from dropsride.utils.logger import LOGGER
from dropsride.utils.unique_generators import unique_id_generator, unique_ref_generator
from dropsride.utils.utilities import is_model_instance_changed

from .models import (
    NextOfKin,
    Profile,
    ReferralBonus,
    RegisteredVehicles,
    Settings,
    VerifiedDocuments,
    Wallet,
)

today = date.today()
User = get_user_model()


@receiver(pre_save, sender=User)
def delete_cache_for_users(sender, instance, *args, **kwargs):
    if is_model_instance_changed(instance):
        if cache.has_key(f"users_{instance.id}") and cache.has_key("all_users"):
            cache.delete(f"users_{instance.id}")
            cache.delete(f"all_users")


@receiver(pre_save, sender=RegisteredVehicles)
def delete_cache_for_users(sender, instance, *args, **kwargs):
    if is_model_instance_changed(instance):
        if cache.has_key(f"users_{instance.user.id}") and cache.has_key("all_users"):
            cache.delete(f"users_{instance.user.id}")
            cache.delete(f"all_users")
        cache.delete_pattern("vehicles:*")


@receiver(pre_save, sender=VerifiedDocuments)
def delete_cache_for_users(sender, instance, *args, **kwargs):
    if is_model_instance_changed(instance):
        if cache.has_key(f"users_{instance.user.id}") and cache.has_key("all_users"):
            cache.delete(f"users_{instance.user.id}")
            cache.delete(f"all_users")
        cache.delete_pattern("documents:*")

@receiver(post_save, sender=VerifiedDocuments)
def expire_license(sender, created, instance, *args, **kwargs):
    if instance.license_exp:
        if instance.license_exp < date.today():
            instance.expired_license()



@receiver(post_save, sender=Wallet)
def calculate_margin(sender, instance, created, **kwargs):
    if cache.has_key(f"users_{instance.user.id}") and cache.has_key("all_users"):
        cache.delete(f"users_{instance.user.id}")
        cache.delete(f"all_users")

    if is_model_instance_changed(instance):
        old_balance = instance.old_balance
        LOGGER.info(old_balance)
        LOGGER.info(instance.balance)
        if instance.balance > old_balance:
            instance.profit = True
            instance.margin = instance.balance - old_balance
            instance.save(update_fields=["profit", "margin"])
        else:
            instance.profit = False
            instance.margin = old_balance - instance.balance
            instance.save(update_fields=["profit", "margin"])


@receiver(post_save, sender=User)
def create_user_relationships(sender, instance, created, **kwargs):
    user = User.objects.get(username=instance.username)
    if cache.has_key(f"users_{instance.id}") and cache.has_key("all_users"):
        cache.delete(f"users_{instance.id}")
        cache.delete(f"all_users")

    if created:
        Token.objects.create(user=instance)
        LOGGER.info("Auth token has been auto generated as well")

        if instance.is_superuser:
            User.objects.filter(username=instance.username).update(
                is_driver=True, gave_consent=True
            )

        Profile.objects.create(user=instance)
        RegisteredVehicles.objects.create(user=instance)
        Wallet.objects.create(user=instance)
        NextOfKin.objects.create(user=instance)
        VerifiedDocuments.objects.create(user=instance)
        ReferralBonus.objects.create(user=instance)
        Settings.objects.create(user=instance)

        LOGGER.info(
            f"[PROFILE, NEXT OF KIN, DOCUMENTS, REFERRAL BONUS AND WALLET RELATIONSHIP CREATED] - {instance.username.title()}"
        )

    if not instance.ref_number:
        ref = unique_ref_generator(instance)
        instance.ref_number = ref
        instance.save(update_fields=["ref_number"])
        LOGGER.info(f"[NEW REFERRAL CODE GENERATED] - {instance.username.title()}")

    if not instance.unique_id:
        id = unique_id_generator(instance)
        instance.unique_id = id
        instance.save(update_fields=["unique_id"])
        LOGGER.info(f"[NEW REGISTRATION CODE GENERATED] - {instance.username.title()}")

    if not instance.is_verified and not instance.is_superuser:
        instance.check_verification()
        LOGGER.info(f"[ACCOUNT VERIFICATION COMPLETED] - {instance.username.title()}")

    if created and not instance.first_name and not instance.last_name:
        # exist for users created from terminal who has no first_name and last_name like superuser
        import pprint

        import requests

        url = "https://api.paystack.co/customer"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        }
        data = {
            "email": instance.email,
            "first_name": instance.email,
            "last_name": instance.email,
        }
        res = requests.request("POST", url, headers=headers, data=data)
        res = res.json()
        pp = pprint.PrettyPrinter(indent=4)
        LOGGER.info(pp.pprint(res))

        if res["message"] == "Customer created":
            user.customer_code = res["data"]["customer_code"]
            user.save(update_fields=["customer_code"])
            LOGGER.info(f"[GENERATED CUSTOMER CODE] - {user.username}")
        else:
            url = f"https://api.paystack.co/customer/{instance.email}"
            headers = {
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            }
            # data = {
            #     "email": instance.email,
            # }
            res = requests.request("GET", url, headers=headers, data=data)
            res = res.json()
            pp = pprint.PrettyPrinter(indent=4)
            LOGGER.info(pp.pprint(res))

            if res["message"] == "Customer retrieved":
                user.customer_code = res["data"]["customer_code"]
                user.save(update_fields=["customer_code"])
                LOGGER.info(f"[GENERATED CUSTOMER CODE] - {user.username}")
            LOGGER.info("[GENERATING CUSTOMER CODE FAILED]")

    elif created and instance.first_name and instance.last_name:
        # exist for users created from terminal who has no first_name and last_name like superuser
        import pprint

        import requests

        url = "https://api.paystack.co/customer"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        }
        data = {
            "email": instance.email,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
        }
        res = requests.request("POST", url, headers=headers, data=data)
        res = res.json()
        pp = pprint.PrettyPrinter(indent=4)
        LOGGER.info(pp.pprint(res))

        if res["message"] == "Customer created":
            user.customer_code = res["data"]["customer_code"]
            user.save(update_fields=["customer_code"])
            LOGGER.info(f"[GENERATED CUSTOMER CODE] - {user.username}")
        else:
            url = f"https://api.paystack.co/customer/{instance.email}"
            headers = {
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            }
            # data = {
            #     "email": instance.email,
            # }
            res = requests.request("GET", url, headers=headers, data=data)
            res = res.json()
            pp = pprint.PrettyPrinter(indent=4)
            LOGGER.info(pp.pprint(res))

            if res["message"] == "Customer retrieved":
                user.customer_code = res["data"]["customer_code"]
                user.save(update_fields=["customer_code"])
                LOGGER.info(f"[GENERATED CUSTOMER CODE] - {user.username}")
            LOGGER.info("[GENERATING CUSTOMER CODE FAILED]")


@receiver(post_save, sender=NextOfKin)
def send_next_of_kin_email_to_verify(sender, instance, created, **kwargs):
    if (
        instance.first_name
        and instance.middle_name
        and instance.last_name
        and instance.email
        and not instance.gave_consent
        and created
    ):
        send_html_email(
            subject=f"NEXT OF KIN VALIDATION",
            template="mail/next_of_kin.html",
            from_email="DROPSRIDE VERIFICATION <noreply@dropsride.com>",
            context={
                "first_name": instance.first_name,
                "long_name": instance.user.long_name,
                "id": instance.id,
                "username": instance.user,
            },
            to_email=[instance.email],
            reply_to="DROPSRIDE SUPPORT <support@dropsride.com>",
            attachment=None,
        )
        LOGGER.info(
            f"[NEXT OF KIN VERIFICATION EMAIL SENT] - {instance.user.long_name}"
        )


@receiver(user_signed_up)
def create_referral_member(request, user, **kwargs):
    if request.session.get("recommender"):
        user_id = request.session.get("recommender")
        recommender = get_object_or_404(User, kwargs={"id": user_id})
        payload = {
            "head": "NEW REFERRAL",
            "body": f"{user.username} has successfully been added to your referral list.",
            "icon": static("vendors/images/favicon/favicon.png"),
            # add url if there is a link to visit from the push notification
            "url": f"http://localhost:8000/{recommender.get_absolute_url()}"
            if not settings.PRODUCTION
            else f"https://dropsride.com/{recommender.get_absolute_url()}",
        }
        user.recommended_by = recommender
        user.save(update_fields=["recommended_by"])
        recommender.ref_bonus.add_bonus()
        request.session.delete("recommender")
        if recommender.settings.push_notification:
            send_user_notification(user=recommender, payload=payload, ttl=1000)

        context = {
            "recommender_first_name": recommender.first_name.title(),
            "user_short_name": user.short_name,
            "recommender_absolute_url": f"http://localhost:8000/{recommender.get_absolute_url()}"
            if not settings.PRODUCTION
            else f"https://dropsride.com/{recommender.get_absolute_url()}",
        }

        if recommender.settings.email_notification:
            send_html_email(
                subject=f"NEW REFERRAL",
                template="mail/referral_bonus.html",
                from_email="DROPSRIDE REFERRAL <noreply@dropsride.com>",
                context=context,
                to_email=[recommender.email],
                reply_to="DROPSRIDE SUPPORT <support@dropsride.com>",
                attachment=None,
            )
            LOGGER.info(f"[REFERRAL CREATED] - {user.long_name}")
    elif user.recommended_by:
        recommender = user.recommended_by
        recommender.ref_bonus.add_bonus()
        payload = {
            "head": "NEW REFERRAL",
            "body": f"{user.username} has successfully been added to your referral list.",
            "icon": static("vendors/images/favicon/favicon.png"),
            # add url if there is a link to visit from the push notification
            "url": f"http://localhost:8000/{recommender.get_absolute_url()}"
            if not settings.PRODUCTION
            else f"https://dropsride.com/{recommender.get_absolute_url()}",
        }
        if recommender.settings.push_notification:
            send_user_notification(user=recommender, payload=payload, ttl=1000)

        context = {
            "recommender_first_name": recommender.first_name.title(),
            "user_short_name": user.short_name,
            "recommender_absolute_url": f"http://localhost:8000/{recommender.get_absolute_url()}"
            if not settings.PRODUCTION
            else f"https://dropsride.com/{recommender.get_absolute_url()}",
        }

        if recommender.settings.email_notification:
            send_html_email(
                subject=f"NEW REFERRAL",
                template="mail/referral_bonus.html",
                from_email="DROPSRIDE REFERRAL <noreply@dropsride.com>",
                context=context,
                to_email=[recommender.email],
                reply_to="DROPSRIDE SUPPORT <support@dropsride.com>",
                attachment=None,
            )
            LOGGER.info(f"[REFERRAL CREATED] - {user.long_name}")
