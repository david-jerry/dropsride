from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.sessions.models import Session
from django.contrib.admin import ModelAdmin

from dropsride.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()

# Register your models here.
class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "middle_name", "last_name", "email", "last_ip", "phone_number", "date_of_birth")}),
        (_("Location info"), {"fields": ("city", "country")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_driver",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "first_name", "middle_name", "last_name",  "email", "phone_number", "is_driver", "is_staff", "is_superuser"]
    search_fields = ["username"]
