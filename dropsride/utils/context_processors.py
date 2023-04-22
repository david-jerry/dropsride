from datetime import date, datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.functional import SimpleLazyObject

from dropsride.currency.models import Currency
from dropsride.utils.logger import LOGGER

User = get_user_model()
dt = datetime.now()
today = date.today()


def context_settings(request):
    webpush = {"group": "sub_user"}
    webpush_settings = getattr(settings, "WEBPUSH_SETTINGS", {})
    vapid_key = webpush_settings.get("VAPID_PUBLIC_KEY")

    hour = dt.hour

    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        # 'drivers': User.objects.filter(is_driver = True).count(),
        # 'riders': User.objects.filter(is_driver = False).count(),
        # 'all_states': Localization.objects.all(),
        "year": dt.year,
        # "APPLICATION_SERVER_KEY": settings.PUSH_NOTIFICATIONS_SETTINGS['APP_SERVER_KEY'],
        "settings": settings,
        "home_url": reverse("home"),
        "google_api_key": settings.GOOGLE_API,
        "webpush": webpush,
        "APPLICATION_SERVER_KEY": vapid_key,
        "currency": Currency.objects.all() if Currency.objects.all().exists() else [],
        "hour": int(hour),
        "site": SimpleLazyObject(lambda: get_current_site(request))
        if not settings.PRODUCTION
        else "localhost:8000",
    }
