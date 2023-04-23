from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.currency.models import Banks, Currency, States
from dropsride.settings.models import Localization
from dropsride.utils.utilities import is_model_instance_changed


@receiver(pre_save, sender=Currency)
def invalidate_other_caches_on_currency_change(sender, instance, **kwargs):
    if is_model_instance_changed(instance):
        cache.clear()


@receiver(post_save, sender=Banks)
def invalidate_cache_if_new_bank_is_added(sender, instance, created, **kwargs):
    if created:
        cache.clear()


@receiver(post_save, sender=States)
def create_default_localization_and_invalidate_cache_on_new_stated_added(
    sender, instance, created, **kwargs
):

    if created:
        cache.clear()
