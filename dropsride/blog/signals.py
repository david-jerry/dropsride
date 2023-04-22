from datetime import date

from django.core.cache import cache
from django.db.models import Max
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.blog.models import News
from dropsride.utils.logger import LOGGER
from dropsride.utils.unique_generators import unique_slug_generator
from dropsride.utils.utilities import is_model_instance_changed


@receiver(pre_save, sender=News)
def clear_post_caches(instance, *args, **kwargs):
    if is_model_instance_changed(instance):
        cache.delete_pattern("news:*")


@receiver(post_save, sender=News)
def create_post_slug_or_post_published_date_signal(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
        LOGGER.info(
            f"[NEWS POST SLUG] Created New Post Slug for {instance.title.title()}"
        )

    if not instance.published_date and instance.draft is False:
        instance.published_date = date.today()
        instance.save()
        LOGGER.info(
            f"[NEWS PUBLISHED DATE] Created Published Date for {instance.title.title()}"
        )
