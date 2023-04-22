from celery import shared_task
from django.conf import settings
from django.core.management import call_command


@shared_task
def get_currency_exchange():
    call_command("get_currency_exchange")
