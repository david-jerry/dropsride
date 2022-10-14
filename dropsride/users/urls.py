from django.urls import path

from dropsride.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,

    driver_switch,
)

app_name = "users"
urlpatterns = [
    path("driver/switch/", view=driver_switch, name="driver-switch"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
