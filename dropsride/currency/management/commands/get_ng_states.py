import pprint
from decimal import Decimal

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from dropsride.currency.models import States
from dropsride.settings.models import Localization
# from requests_html import HTMLSession
from dropsride.utils.logger import LOGGER


class Command(BaseCommand):
    """
    Retreives all nigerian states
    """

    help = _("Add all nigerian states")

    def handle(self, *args, **kwargs):
        url = str(f"{settings.YOUVERIFY_ENV}/v2/api/states")
        headers = {
            "token": str(settings.YOUVERIFY_API),
        }

        res = requests.request("GET", url, headers=headers)
        res = res.json()
        pp = pprint.PrettyPrinter(indent=4)
        LOGGER.info(pp.pprint(res))

        if res["statusCode"] == 200:
            for response in res["data"]:
                try:
                    instance = States.objects.get_or_create(state=response["state"], country_iso="NG")
                    Localization.objects.create(state=instance)
                    LOGGER.info(f"Successfully added {response['state']}")
                except Exception as e:
                    LOGGER.error(e)
        else:
            LOGGER.error(f"Nigerian States Not Updated")

        self.stdout.write("Got all Nigeria States Details")
