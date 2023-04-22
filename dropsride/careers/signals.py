from datetime import date

from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.core.tasks import send_html_email
from dropsride.utils.logger import LOGGER
from dropsride.utils.unique_generators import unique_slug_generator
from dropsride.utils.utilities import is_model_instance_changed


@receiver(post_save, sender=Teams)
def create_team_slug(instance, created, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
        LOGGER.info("[CAREERS DEPARTMENT SLUG] Created New Department Slug")


@receiver(post_save, sender=Careers)
def create_career_slug(instance, *args, created, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
        LOGGER.info("[CAREERS SLUG] Created New Career Slug")

    if instance.published_date is None and instance.draft is False:
        instance.published_date = date.today()
        instance.save()
        LOGGER.info(
            f"[CAREER PUBLISHED DATE] Created Published Date for {instance.title.title()}"
        )


@receiver(post_save, sender=Applicants)
def send_applicant_email(instance, created, *args, **kwargs):
    if created:
        send_html_email(
            subject=instance.position.title.upper(),
            template="mails/career_mail.html",
            from_email="careers@dropsride.com",
            context=None,
            to_email=[instance.email],
            reply_to="careers@dropsride.com",
        )
        LOGGER.info(f"[APPLICANT EMAIL SENT] Sent email to applicant")
