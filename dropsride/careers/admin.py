from django.contrib import admin

# Register your models here.
from .models import Careers, Applicants, Teams

admin.site.register(Careers)
admin.site.register(Applicants)
admin.site.register(Teams)
