import os
import random


from datetime import datetime


from django.db.models import Max
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.files import File

from dropsride.utils.unique_generators import unique_slug_generator
from dropsride.utils.logger import LOGGER

from pydub import AudioSegment
from pathlib import Path

from dropsride.blog.models import News


@receiver(pre_save, sender=News)
def create_post_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        LOGGER.info(f"[NEWS POST SLUG] Created New Post Slug for {instance.title.title()}")



@receiver(post_save, sender=News)
def create_published_date(instance, created, *args, **kwargs):
    if instance.published_date is None and instance.draft is False:
        instance.published_date = datetime.now()
        instance.save()
        LOGGER.info(f"[NEWS PUBLISHED DATE] Created Published Date for {instance.title.title()}")
