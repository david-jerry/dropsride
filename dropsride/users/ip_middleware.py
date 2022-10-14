from __future__ import annotations
from inspect import iscoroutinefunction

import re
import time
import asyncio
import datetime
import geocoder

from ipware import get_client_ip
from typing import Any, Awaitable, Callable
from urllib.parse import unquote

from django.conf import settings
from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.utils.deprecation import MiddlewareMixin
from django.utils.decorators import sync_and_async_middleware

from datetime import datetime, time

from dropsride.utils.logger import LOGGER
from dropsride.sitesettings.models import (
    SiteSettings,
    APIKeys,
    SocialSiteSettings,
    DriverSettings,
)

now = datetime.now()
now_time = now.time()

User = get_user_model()
PRIVATE_IPS_PREFIX = ("10.", "172.", "192.", "127.")


@sync_and_async_middleware
def IpAddressMiddleware(get_response):
    # sync_capable = False
    # async_capable = True
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request):
            x_forwarded_for = await request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                proxies = x_forwarded_for.split(",")
                while len(proxies) > 0 and proxies[0].startswith(PRIVATE_IPS_PREFIX):
                    proxies.pop(0)
                # take the first ip which is not a private one (of a proxy)
                if len(proxies) > 0:
                    ip = proxies[0]
            else:
                if settings.PRODUCTION:
                    ip = await request.META.get("REMOTE_ADDR")
                else:
                    ip = "8.8.8.8"

            request.ip = ip

            # loc = await geocoder.ip(ip)
            # request.city = loc.city
            # request.state = loc.state
            # request.country = loc.country
            # request.latlng = loc.latlng

            if now_time >= time(4, 00) and now_time < time(12, 00):
                greeting = "Good Morning"
                sleep = False
            elif now_time >= time(12, 00) and now_time < time(17, 00):
                greeting = "Good Afternoon"
                sleep = False
            elif now_time >= time(17, 00) and now_time < time(22, 00):
                greeting = "Good Evening"
                sleep = False
            elif now_time >= time(22, 00):
                greeting = "Good Night"
                sleep = True
            else:
                greeting = "Welcome"
                sleep = False

            request.sleep = sleep
            request.geetings = greeting

            response = await get_response(request)
            LOGGER.info("ASYNC MIDDLEWARE RUNNING")
            return response

    else:

        def middleware(request):
            client_ip, is_routable = get_client_ip(request)
            LOGGER.info(f"CLIENT IP: {client_ip}")
            if client_ip is None:
                x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
                if x_forwarded_for:
                    proxies = x_forwarded_for.split(",")
                    while len(proxies) > 0 and proxies[0].startswith(
                        PRIVATE_IPS_PREFIX
                    ):
                        proxies.pop(0)
                    # take the first ip which is not a private one (of a proxy)
                    if len(proxies) > 0:
                        ip = proxies[0]
                else:
                    if settings.PRODUCTION:
                        ip = request.META.get("REMOTE_ADDR")
                    else:
                        ip = "37.19.199.141"
            else:
                if is_routable:
                    ip = client_ip
                else:
                    ip = "37.19.199.141"
            request.ip = ip

            if SiteSettings.objects.filter(id=1).exists():
                sitesettings = SiteSettings.objects.first()
                request.sitesettings = sitesettings
            else:
                request.sitesettings = None

            if APIKeys.objects.filter(id=1).exists():
                apikeys = APIKeys.objects.first()
                request.api_keys = apikeys
            else:
                request.api_keys = None

            if SocialSiteSettings.objects.filter(id=1).exists():
                social = SocialSiteSettings.objects.first()
                request.social = social
            else:
                request.social = None

            if DriverSettings.objects.filter(id=1).exists():
                driver_settings = DriverSettings.objects.first()
                request.driver_settings = driver_settings
            else:
                request.driver_settings = None


            # loc = geocoder.ip(ip)
            # request.city = loc.city
            # request.state = loc.state
            # request.country = loc.country
            # request.latlng = loc.latlng

            if now_time >= time(4, 00) and now_time < time(12, 00):
                request.greeting = "Good Morning"
                request.sleep = False
            elif now_time >= time(12, 00) and now_time < time(17, 00):
                request.greeting = "Good Afternoon"
                request.sleep = False
            elif now_time >= time(17, 00) and now_time < time(22, 00):
                request.greeting = "Good Evening"
                request.sleep = False
            elif now_time >= time(22, 00):
                request.greeting = "Good Night"
                request.sleep = True
            else:
                request.greeting = "Welcome"
                request.sleep = False

            response = get_response(request)
            LOGGER.info("SYNC MIDDLEWARE RUNNING")
            return response

    return middleware
