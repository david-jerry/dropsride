from django.contrib import admin
from .models import (
    Riders,
    RiderSavedAddress,
    RiderWallet,
    RiderTransactionHistory,
)
# Register your models here.
admin.site.register(Riders)
admin.site.register(RiderSavedAddress)
admin.site.register(RiderWallet)
admin.site.register(RiderTransactionHistory)
