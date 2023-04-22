import asyncio
import pprint
from datetime import date

import requests
from asgiref.sync import sync_to_async
from django.conf import settings
from django.http import HttpRequest
from django.utils.decorators import sync_and_async_middleware
from django.utils.deprecation import MiddlewareMixin

from dropsride.tickets.models import TicketSubscription
from dropsride.utils.logger import LOGGER

today = date.today()


class UserSubscribedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and request.user.is_driver
            and TicketSubscription.objects.filter(
                driver=request.user, active=True
            ).exists()
        ):
            request.subscribed = True
            ticket = TicketSubscription.objects.filter(
                driver=request.user, active=True
            ).first()
            ticket.deactivate_ticket()
        else:
            request.subscribed = False
        response = self.get_response(request)
        return response
