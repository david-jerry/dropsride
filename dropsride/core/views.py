import json

import googlemaps
from asgiref.sync import async_to_sync, sync_to_async
from async_googlemaps import AsyncClient
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.db import transaction
from django.http.response import (  # , HttpResponsePermanentRedirect
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.views.generic import FormView
from notifications.models import Notification
from webpush import send_user_notification

from dropsride.core.forms import ContactForm
from dropsride.core.tasks import send_html_email
from dropsride.tickets.models import TicketPlans
from dropsride.utils.logger import LOGGER

User = get_user_model()
gmaps = googlemaps.Client(key=settings.GOOGLE_API)
# session = aiohttp.ClientSession()
# gmaps = AsyncClient(session, key=settings.GOOGLE_API)


@require_GET
def mark_read(request, *args, **kwargs):
    notif = Notification.objects.get(id=kwargs.get("id"))
    notif.mark_as_read()
    return JsonResponse(
        status=200, data={"message": f"{notif.verb.title} marked as read"}
    )


# @transaction.atomic()
def save_cordinates(request, *args, **kwargs):
    lon = 7.033611 if not settings.PRODUCTION else float(kwargs.get("long"))
    lat = 4.824167 if not settings.PRODUCTION else float(kwargs.get("lat"))
    location = Point(lon, lat)

    if request.user.is_authenticated:
        # thread sensitive means running on the same main thread while thread sensitive false mean can run in a new thread
        User.objects.filter(id=request.user.id).update(location=location)
        LOGGER.info(f"saved user location")

    res = gmaps.reverse_geocode((lat, lon))
    LOGGER.info(res)
    get_state = res[1]["address_components"][2]["long_name"]
    LOGGER.info(f"Current State: {get_state}")

    if request.user.is_authenticated:
        if (
            TicketPlans.objects.filter(
                localization__state__state__iexact=get_state
            ).exists()
            and request.user.get_user_cards
        ):
            local = TicketPlans.objects.get(
                localization__state__state__iexact=get_state
            )  # TicketPlans.objects.get(localization__state__state__iexact=get_state)
            amount = local.pay_amount
            if request.user.wallet.pay_amount == amount:
                return JsonResponse(
                    status=200,
                    data={
                        "buyTicket": request.subscribed,
                        "amount": amount,
                        "state": get_state,
                    },
                )
            else:
                return JsonResponse(
                    status=200,
                    data={
                        "buyTicket": request.subscribed,
                        "amount": amount,
                        "state": get_state,
                    },
                )
        return JsonResponse(
            status=200,
            data={"buyTicket": request.subscribed, "amount": 0, "state": get_state},
        )
    return JsonResponse(
        status=200,
        data={"buyTicket": request.subscribed, "amount": 0, "state": get_state},
    )


@require_GET
def ref_home(request, *args, **kwargs):
    try:
        ref = str(kwargs.get("ref_number"))
        recommended_by = User.objects.get(ref_number=ref)
        request.session["recommender"] = recommended_by.id
    except:
        pass
    return render(request, "pages/home.html")


class SupportCreateView(FormView):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form": form}
        return render(request, "pages/contact.html", context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            valid_data = form.cleaned_data
            send_html_email.delay(
                subject="SUPPORT MAIL",
                template="mails/support.html",
                from_email=f"{valid_data['company'].upper() or valid_data['name'].title()} <noreply@dropsride.com>",
                context={
                    "name": valid_data["name"].title(),
                    "phone": valid_data["phone"],
                    "email": valid_data["email"],
                    "message": valid_data["message"],
                },
                to_email=["support@dropsride.com"],
                reply_to=["support@dropsride.com"],
                attachment=None,
            )
            return JsonResponse(
                status=200,
                data={
                    "message": "Support Mail Successfully Sent",
                    "title": "Support Mail",
                },
            )
        return JsonResponse(
            status=500,
            data={
                "message": "Support Mail Failed to validate",
                "title": "SUPPORT EMAIL FAILED",
            },
        )


support = SupportCreateView.as_view()

# def drivers(request):
#     user = request.user
#     list_drivers = TicketSubscription.objects.filter(status=TicketSubscription.ACTIVE, driver__is_active=True, driver__userState=user.userState, driver__is_driver=True, driver__on_a_ride=False, driver__location__distance_lt=(user.location, Distance(m=15000)))[:30]#.values('driver__location__x', 'driver__location__y', 'driver__username', 'driver__userState')[:30]
#     drivers = [{
#         'username':i.driver.username,
#         'lat': i.driver.latitude,
#         'lng': i.driver.longitude,
#     } for i in list_drivers]
#     LOGGER.info(drivers)
#     if not user.is_authenticated:
#         return JsonResponse(status=400, data={'message':"User not authenticated"})
#     elif len(drivers) > 0:
#         return JsonResponse(status=200, data={'data':drivers})
#     else:
#         return JsonResponse(status=400, data={'message':"No Available Driver Right Now. Please check back later"})


@require_POST
@csrf_exempt
def send_user_push_notification(request):
    try:
        body = request.POST.get("message")
        user = User.objects.get(username=request.POST.get("username"))
        head = "ADMINISTRATIVE NOTIFICATION"
        payload = {
            "head": head,
            "body": body,
            "icon": static("vendors/images/favicon/favicon.png"),
        }
        send_user_notification(user=user, payload=payload, ttl=1000)
        return JsonResponse(status=200, data={"message": "Notification sent"})
    except TypeError:
        return JsonResponse(
            status=500, data={"message": "An Error occurred while sending notification"}
        )


@require_POST
@csrf_exempt
def send_notification(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except ValueError:
        return HttpResponse(status=400)

    try:
        head = data.pop("head")
        body = data.pop("body")
        payload = {
            "head": head,
            "body": body,
            "icon": static("vendors/images/favicon/favicon.png"),
        }
        send_user_notification(user=request.user, payload=payload, ttl=1000)
        return JsonResponse(status=200, data={"message": "Notification sent"})
    except TypeError:
        return JsonResponse(
            status=500, data={"message": "An Error occurred while sending notification"}
        )


@require_http_methods(["GET"])
def offline_view(request):
    title = "Offline Page"
    description = "You currently have no network, so we are serving you this offline page showcasing our top rated podcasts to listen to for free"
    author = "Jeremiah E David (http://darkcodr.codes)"
    can_link = reverse("offline")
    twitter_handle = "@darkcodr_codes"
    template = "pages/offline.html"
    context = {
        "title": title,
        "description": description,
        "author": author,
        "can_link": can_link,
        "twitter_handle": twitter_handle,
        "offline": True,
    }
    return render(request, template, context)


@require_http_methods(["GET"])
def service_worker(request):
    sw_path = settings.APPS_DIR / "static/bundles" / "sw.js"
    response = HttpResponse(open(sw_path).read(), content_type="application/javascript")
    return response


@require_http_methods(["GET"])
def index_map(request):
    sw_path = settings.APPS_DIR / "static/bundles" / "index.html"
    response = HttpResponse(open(sw_path).read(), content_type="text/html")
    return response
