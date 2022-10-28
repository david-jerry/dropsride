from django.contrib import admin
from .models import (
    Company,
    CompanySavedAddress,
    CompanyWallet,
    CompanyTransactionHistory
)
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanySavedAddress)
admin.site.register(CompanyWallet)
admin.site.register(CompanyTransactionHistory)
