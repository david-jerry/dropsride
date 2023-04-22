from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.tickets.models import TicketPlans
from dropsride.utils.logger import LOGGER
from dropsride.utils.unique_generators import unique_slug_generator
from dropsride.utils.utilities import (
    is_model_instance_changed,
    is_uuid_model_instance_changed,
)

from .models import CarType, Localization


@receiver(pre_save, sender=Localization)
def invalidate_other_caches_on_localization_change(sender, instance, **kwargs):
    if is_uuid_model_instance_changed(instance):
        cache.clear()


@receiver(post_save, sender=Localization)
def create_plan(sender, instance, created, **kwargs):
    if created:
        cache.clear()

    LOGGER.info("INITIALIZING TICKET PLANS")
    if not TicketPlans.objects.filter(localization=instance).exists():
        LOGGER.info("CREATING PLANS")
        TicketPlans.objects.create(localization=instance)
        LOGGER.info("CREATED PLANS")


@receiver(post_save, sender=CarType)
def create_cartype_slug(instance, created, *args, **kwargs):
    if created:
        cache.clear()

    if not instance.slug:
        cache.clear()
        instance.slug = unique_slug_generator(instance)
        instance.save()
        LOGGER.info(
            f"[CAR TYPE SLUG] Created New CAR Slug for {instance.title.title()}"
        )
