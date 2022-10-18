from decimal import Decimal

import requests
import pprint

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

# from requests_html import HTMLSession
from dropsride.utils.logger import LOGGER
from dropsride.currency.models import Banks


class Command(BaseCommand):
    """
    Retreives all the banks in Nigeria
    """

    help = _("Collect current bank rates")

    def handle(self, *args, **kwargs):
        url = str("https://api.paystack.co/bank")

        params = {
            "perPage":100,
            "country":"nigeria",
        }

        if not settings.PRODUCTION:
            headers = {
                'Authorization': str(settings.PAYSTACK_TEST_SK),
            }
        else:
            headers = {
                'Authorization': str(settings.PAYSTACK_LIVE_SK),
            }

        res = requests.request("GET", url, headers=headers, params=params)
        res = res.json()
        pp = pprint.PrettyPrinter(indent=4)
        LOGGER.info(pp.pprint(res))

        if res['status']:
            for response in res['data']:
                Banks.objects.create(
                    name=response['name'],
                    slug=response['slug'],
                    lcode=response['longcode'],
                    code=response['code'],
                    country_iso=response['country']
                )
                # LOGGER.info(f"Created Bank: {response['name']}")
            if 'meta' in res:
                params = {
                    "perPage":100,
                    "country":"nigeria",
                    'next':res['data']['next']
                }


                res = requests.request("GET", url, headers=headers, params=params)
                res = res.json()

                if res['status']:
                    for response in res['data']:
                        Banks.objects.create(
                            name=response['name'],
                            slug=response['slug'],
                            lcode=response['longcode'],
                            code=response['code'],
                            country_iso=response['country']
                        )
                        LOGGER.info(f"Created Bank: {response['name']}")
                        if "meta" in res:
                            params = {
                                "perPage":100,
                                "country":"nigeria",
                                'next':res['data']['next']
                            }


                            res = requests.request("GET", url, headers=headers, params=params)
                            res = res.json()

                            if res['status']:
                                for response in res['data']:
                                    Banks.objects.create(
                                        name=response['name'],
                                        slug=response['slug'],
                                        lcode=response['longcode'],
                                        code=response['code'],
                                        country_iso=response['country']
                                    )
                                    LOGGER.info(f"Created Bank: {response['name']}")
        else:
            LOGGER.error(f"NGN rate not updated")



        self.stdout.write("Gotten all Nigeria Bank Details")



