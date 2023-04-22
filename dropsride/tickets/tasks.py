from datetime import date

from celery import shared_task
from django.utils import timezone

from dropsride.tickets.models import TicketSubscription


@shared_task
def set_ticket_inactive():
    today = date.today()
    expired_tickets = TicketSubscription.objects.filter(
        active=True, expiry_date__lt=today
    )
    for ticket in expired_tickets:
        ticket.deactivate_ticket()
