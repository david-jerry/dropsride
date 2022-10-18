from django.urls import path

from dropsride.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_update_photo,
    user_update_social_accounts,
    user_update_address,
    verify_phone_number,
    add_next_of_kin,
    add_account_details,
    add_new_card,
    driver_switch,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("driver/switch/", view=driver_switch, name="driver-switch"),
    path("verify-phone/", view=verify_phone_number, name="verify_phone"),
    path("add/nok/", view=add_next_of_kin, name="add_next_of_kin"),
    path("add/bank-account/", view=add_account_details, name="add_bank_details"),
    path("add/card/", view=add_new_card, name="add_new_card"),
    path("~update/", view=user_update_view, name="update"),
    path("~update/address/", view=user_update_address, name="update_address"),
    path("~update/dp/", view=user_update_photo, name="update_image"),
    path(
        "~update/social-accounts/",
        view=user_update_social_accounts,
        name="update_social_account",
    ),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
