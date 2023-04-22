import pprint

import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from dropsride.rides.models import Trips
from dropsride.utils.logger import LOGGER

# @receiver(post_save, sender=Trips)
# def update_gross_price(sender, instance, created, **kwargs):
#     if instance.amount and instance.car_type and not instance.gross_price:
#         gross = instance.amount + instance.car_type.amount
#         Trips.ojects.filter(uuid=instance.uuid).update(gross_total=gross)
#         LOGGER.info("UPDATED TOTAL GROSS PRICE")
