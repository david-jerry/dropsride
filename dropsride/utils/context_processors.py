import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
from django.urls import reverse

# from dropsride.pages.models import LegalPages, StaticPages
from dropsride.currency.models import Currency
from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.sitesettings.models import Localization
from dropsride.utils.logger import LOGGER

from taggit.models import Tag

User = get_user_model()
dt = datetime.datetime.now()


def context_settings(request):

    webpush = {"group":"sub_user"}
    webpush_settings = getattr(settings, "WEBPUSH_SETTINGS", {})
    vapid_key = webpush_settings.get("VAPID_PUBLIC_KEY")
    # LOGGER.info(f"VAPID_PUBLIC_KEY: {vapid_key}")




    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        'drivers': User.objects.filter(is_driver = True).count(),
        'riders': User.objects.filter(is_driver = False).count(),
        'states': Localization.objects.all().count(),
        # 'all_states': Localization.objects.all(),
        'year': dt.year,
        # "APPLICATION_SERVER_KEY": settings.PUSH_NOTIFICATIONS_SETTINGS['APP_SERVER_KEY'],
        "settings": settings,
        'home_url': reverse('home'),
        'google_api_key': settings.GOOGLE_API,
        'webpush': webpush,
        'APPLICATION_SERVER_KEY': vapid_key,
        "currency": Currency.objects.all() if Currency.objects.all().exists() else None,



        "tags": Tag.objects.all()[:12] if Tag.objects.all().exists() else None,

        'site': SimpleLazyObject(lambda: get_current_site(request)) if not settings.PRODUCTION else "localhost:8000",
    }
