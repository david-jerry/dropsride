from datetime import timedelta
from allauth.socialaccount.signals import pre_social_login, social_account_added
from dropsride.companies.models import Company

import geocoder

from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from dropsride.admins.models import Admins
from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.users.models import UserNextOfKin, UserSocialAccounts, VerifiedPhone
from dropsride.utils.logger import LOGGER
from dropsride.utils.unique_generators import random_code_generator

from paystackapi.customer import Customer

from webpush import send_user_notification, send_group_notification
from messente_api import OmnimessageApi, SMS, Omnimessage, Configuration, ApiClient
from messente_api.rest import ApiException

User = get_user_model()


@receiver(post_save, sender=VerifiedPhone)
def create_random_code(instance, created, **kwargs):
    if not instance.code and not instance.user.is_superuser and instance.created:
        instance.code = random_code_generator(instance)
        configuration = Configuration()
        configuration.username = settings.MESSENTE_API_USERNAME
        configuration.password = settings.MESSENTE_API_PASSWORD
        domain = "https://www.dropsride.com" if settings.PRODUCTION else "localhost:8000"
        link = reverse("sms_verify", kwargs={"code":instance.code, "user":instance.user})

        api_instance = OmnimessageApi(ApiClient(configuration))

        sms = SMS(sender="Drops Technology Limited", text=f"please find attached your verification code: {instance.code}\n\nYou can also verify by clicking the link below\n\n{domain}{link}")

        omnimessage = Omnimessage(messages=tuple([sms]), to=instance.user.phone_number)

        try:
            response = api_instance.send_omnimessage(omnimessage)
            payload = {
                'head': "VERIFICATION CODE SENT",
                'body': f"please find attached your verification code: {instance.code}\n\nYou can also verify by clicking the link below\n\n{domain}{link}",
                'icon': static('vendors/images/favicon/favicon.png'),
                # add url if there is a link to visit from the push notification
                'url': f"{domain}{link}",
            }
            send_user_notification(user=instance.user, payload=payload, ttl=1000)

            LOGGER.info(
                "[PHONE VERIFICATION SUCCESS] Successfully sent Omnimessage with id: %s that consists of the following messages:"
                % response.omnimessage_id
            )
            for message in response.messages:
                LOGGER.info(message)
        except ApiException as exception:
            LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)


@receiver(post_save, sender=User)
def create_user_relationship_signal(instance, created, **kwargs):
    if not instance.ref_link and not instance.is_superuser:
        res = Customer.objects.create(first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
        LOGGER.info(res)
        instance.ref_link = res.customer_code
        LOGGER.info(f"[NEW USER] Created New Referral/Customer Link for {instance.username}")

    if instance.is_driver and not instance.is_superuser:
        Drivers.objects.create(user=instance)
        LOGGER.info(f"[NEW DRIVER] Created New Driver Account Relationships for {instance.username}")

    if instance.is_company and not instance.is_superuser:
        Company.objects.create(user=instance)
        LOGGER.info(f"[NEW BUSINESS ACCOUNT] Created New Company Account Relationships for {instance.username}")

    if instance.is_staff and not instance.is_superuser:
        Admins.objects.create(user=instance)
        LOGGER.info(f"[NEW STAFF] Created New Administrator Account Relationships for {instance.username}")

    if created:
        if instance.is_superuser:
            instance.is_driver = True
            instance.is_company = True
            instance.gave_consent = True
        UserSocialAccounts.objects.create(user=instance)
        VerifiedPhone.objects.create(user=instance)
        UserNextOfKin.objects.create(user=instance)
        LOGGER.info(f"[NEW USER] Created New Social Account Relationships for {instance.username}")

    if not instance.is_driver and not instance.is_superuser:
        Riders.objects.create(user=instance)
        LOGGER.info(f"[NEW RIDER] Created New Rider Account Relationships for {instance.username}")


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    assert hasattr(request, 'ip') # check if user is logged in

    last_ip = user.last_ip if user.last_ip else None
    loc = geocoder.ip(request.ip)

    if request.ip != last_ip and last_ip != None:
        User.objects.filter(username=user.username).update(last_ip=request.ip, city=loc.city, country=loc.country.upper())
        payload = {
            'head': "ACCOUNT SECURITY",
            'body': f"You account was logged in with a new IP Address: {request.ip}, in a new City: {loc.city}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': request._current_scheme_host + f"/users/{user.username}",
        }
        send_user_notification(user=user, payload=payload, ttl=1000)

        message = f"Dear {user.get_full_name()},\n Please ignore if you are the one signing in from {loc.city}, {loc.country} with this ip {request.ip}"

        html_message = f"""
        <strong>Dear {user.get_full_name()}</strong>
        <br>
        <br>
        <p>Please ignore if you are the one signing in from <strong>{loc.city}, {loc.country}</strong> with this ip <strong>{request.ip}</strong></p>
        <br>
        <br>
        """
        msg = EmailMultiAlternatives("New IP Login", message, "security@dropsride.com", [request.user.email])
        msg.attach_alternative(mark_safe(html_message), "text/html")
        msg.content_subtype = "html"
        msg.send()
        LOGGER.info(f"New Ip {user.last_ip} Updated for {user.username.title()} account")
    elif last_ip == None:
        User.objects.filter(username=user.username).update(last_ip=request.ip)
        LOGGER.info(f"[NEW IP] New Ip {user.last_ip} Added to {user.username.title()} account")
    else:
        LOGGER.info(f"[NEW IP] New Login from IP:{user.last_ip} for {user.username.title()} account")


# social_account_added
@receiver(pre_social_login)
def create_social_account_relationships(request, sociallogin, *args, **kwargs):
    if sociallogin.is_existing:
        user = sociallogin.user
        LOGGER.info(f"[SOCIAL ACCOUNT USER] : {user.username}")
        try:
            existing_user = User.objects.get(username=user.username)
            UserSocialAccounts.objects.get(user=user)
        except UserSocialAccounts.DoesNotExist:
            UserSocialAccounts.objects.create(user=user)
            LOGGER.info(f"[NEW USER SOCIAL ACCOUNT] Created New Social Account Relationships for {user.username}")


@receiver(social_account_added)
def add_profile_picture(request, sociallogin, *args, **kwargs):
    user = sociallogin.user
    if User.objects.filter(email=user.email).exists():
        existing_user = User.objects.get(email=user.email)
        if not existing_user.image or not existing_user.first_name or not existing_user.last_name:
            existing_user.first_name = sociallogin.account.extra_data.get("first_name")
            existing_user.last_name = sociallogin.account.extra_data.get("last_name")
            existing_user.image = sociallogin.account.get_avatar_url()
            existing_user.save()
            LOGGER.info(f"[NEW USER SOCIAL ACCOUNT] Added Profile Picture for {user.username}")
    elif not User.objects.filter(email=user.email).exists():
        new_user = User.objects.create_user(first_name=sociallogin.account.extra_data.get("first_name"), image=sociallogin.account.get_avatar_url(), last_name=sociallogin.account.extra_data.get("last_name"), email=user.email, username=user.username, password=f"ACC{user.username}{user.id}")
        UserSocialAccounts.objects.create(user=new_user)
        LOGGER.info(f"[NEW USER SOCIAL ACCOUNT] Created New User and Social Account Relationships for {user.username}")
