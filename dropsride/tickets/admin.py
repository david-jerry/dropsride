from django.contrib import admin

from .models import TicketPlans, TicketSubscription

# Register your models here.
admin.site.register(TicketPlans)
admin.site.register(TicketSubscription)
