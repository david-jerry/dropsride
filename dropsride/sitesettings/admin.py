from django.contrib import admin
from .models import (
    Localization,
    SiteSettings,
    SocialSiteSettings,
    DriverSettings,
    VehicleType,
    APIKeys,
)

# Register your models here.
admin.site.register(Localization)
admin.site.register(SiteSettings)
admin.site.register(SocialSiteSettings)
admin.site.register(VehicleType)
admin.site.register(DriverSettings)
admin.site.register(APIKeys)

