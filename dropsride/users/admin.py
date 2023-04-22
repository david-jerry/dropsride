from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dropsride.users.forms import UserAdminChangeForm, UserAdminCreationForm
from dropsride.users.models import (
    BankAccount,
    NextOfKin,
    Profile,
    ReferralBonus,
    RegisteredVehicles,
    SavedCards,
    Settings,
    VerifiedDocuments,
    Wallet,
)

User = get_user_model()

admin.site.register(Profile)
admin.site.register(RegisteredVehicles)
admin.site.register(ReferralBonus)
admin.site.register(Settings)
admin.site.register(SavedCards)
admin.site.register(BankAccount)
admin.site.register(Wallet)
admin.site.register(NextOfKin)
admin.site.register(VerifiedDocuments)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("ID Fields"), {"fields": ("unique_id", "ref_number")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "middle_name", "last_name", "email", "gender")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_driver",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "gave_consent",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = [
        "username",
        "unique_id",
        "ref_number",
        "customer_code",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "gave_consent",
        "on_a_ride",
        "is_active",
        "is_driver",
        "is_staff",
        "is_superuser",
    ]
    list_editable = [
        "first_name",
        "middle_name",
        "last_name",
        "customer_code",
        "email",
        "on_a_ride",
        "is_active",
        "is_driver",
        "is_staff",
        "is_superuser",
    ]
    search_fields = ["first_name", "middle_name", "last_name", "email"]
