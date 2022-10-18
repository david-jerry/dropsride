import os
import random


from datetime import datetime


from django.db.models import Max
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.files import File
from django.core.mail import send_mail
from django.utils.safestring import mark_safe

from dropsride.utils.unique_generators import unique_slug_generator
from dropsride.utils.logger import LOGGER

from dropsride.careers.models import Careers, Applicants


@receiver(pre_save, sender=Careers)
def create_career_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        LOGGER.info("[CAREERS SLUG] Created New Career Slug")



@receiver(post_save, sender=Applicants)
def send_applicant_email(instance, created, *args, **kwargs):
    if created:
        message = f"Thank you for applying to the job position. \n\nWe shall be contacting you soon with further instructions if you meet our requirements."
        send_mail(subject=f"[{instance.position.title.upper()}]", message=mark_safe(message), from_email="careers@dropsride.com", recipient_list=[instance.email], fail_silently=False)
        LOGGER.info(f"[APPLICANT EMAIL SENT] Sent email to applicant")
