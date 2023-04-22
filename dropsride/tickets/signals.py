from datetime import date

from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.tickets.models import TicketPlans, TicketSubscription
from dropsride.utils.utilities import is_model_instance_changed


@receiver(pre_save, sender=TicketPlans)
def clear_cache(sender, instance, **kwargs):
    if is_model_instance_changed(instance):
        transaction_cache_keys = [key for key in cache.keys() if "tickets" in key]
        for k in transaction_cache_keys:
            cache.delete(k)


@receiver(pre_save, sender=TicketSubscription)
def clear_cache(sender, instance, **kwargs):
    if is_model_instance_changed(instance):
        transaction_cache_keys = [key for key in cache.keys() if "tickets" in key]
        for k in transaction_cache_keys:
            cache.delete(k)


# @receiver(post_save, sender=TicketSubscription)
# def set_expiry_date(sender, instance, created, **kwargs):
#     """
#     After a driver subscribes to a ticket, create an expiry date to a day in the future
#     """
#     if created:
#         plan = instance.plan
#         expiry_date = today + timedelta(days=plan.duration)
#         instance.expiry_date = expiry_date
#         instance.save()
