from django.contrib import admin

from .models import CarType, Localization

# Register your models here.
admin.site.register(Localization)
admin.site.register(CarType)
