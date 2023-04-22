from django.contrib import admin

from .models import Banks, Currency, States

# Register your models here.
admin.site.register(Currency)
admin.site.register(Banks)
admin.site.register(States)
