from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse


class ServiceWorkerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #  expires=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        response = self.get_response(request)
        webpush_settings = getattr(settings, "WEBPUSH_SETTINGS", {})
        vapid_key = webpush_settings.get("VAPID_PUBLIC_KEY")
        response.set_cookie(
            "APPLICATION_SERVER_KEY",
            value=vapid_key,
            max_age=None,
            path="/",
            domain=None,
            secure=False,
            httponly=False,
            samesite=None,
        )
        response.set_cookie(
            "SEND_NOTIFICATION_LINK",
            value=reverse("send_notification"),
            max_age=None,
            path="/",
            domain=None,
            secure=False,
            httponly=False,
            samesite=None,
        )
        response.set_cookie(
            "CREATE_WP_DEVICE",
            value=reverse("save_webpush_info"),
            max_age=None,
            path="/",
            domain=None,
            secure=False,
            httponly=False,
            samesite=None,
        )
        return response
