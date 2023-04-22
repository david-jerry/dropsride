from django.urls import path

from dropsride.users.views import (
    all_users,
    get_admin_detail,
    get_all_cards,
    get_banks,
    get_cards,
    get_currency,
    get_detail,
    get_kin,
    get_profile_card,
    get_verified,
    search_users,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("get-process/", view=get_verified, name="get_verified"),
    path("get-profile-card/", view=get_profile_card, name="get_profile_card"),
    path("", all_users, name="list"),
    path("", search_users, name="search_users"),
    # path("cards/verifypayment/<ref>/", verifyCardpayment, name="card-verify"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("get-currency/", view=get_currency, name="get_currency"),
    path("get-kin/", view=get_kin, name="get_kin"),
    path("get-detail/", view=get_detail, name="get_detail"),
    path("get-detail/<str:username>/", view=get_admin_detail, name="get_admin_detail"),
    path("get-cards/", view=get_all_cards, name="get_all_cards"),
    path("get-cards/<auth_code>/", view=get_cards, name="get_cards"),
    path("get-banks/", view=get_banks, name="get_banks"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
