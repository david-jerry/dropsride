from django.contrib import admin
from .models import (
    Drivers,
    Subscription,
    DriverWallet,
    DriverTransactionHistory
)
# Register your models here.
admin.site.register(Drivers)
admin.site.register(Subscription)
admin.site.register(DriverWallet)
admin.site.register(DriverTransactionHistory)
