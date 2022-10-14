from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from dropsride.admins.views import (
    admin_dashboard,
    filter_documents,

    all_users,
    all_drivers,
    all_riders,

    admin_deactivate_driver,
    admin_switch,
    admin_deactivate_rider,
    admin_end_user_session,

    add_new_driver,
    add_new_rider,
    add_new_admin
)

app_name = "admins"
urlpatterns = [
    path("", view=staff_member_required(admin_dashboard), name="dashboard"),


    path("users/", view=staff_member_required(all_users), name="all_users"),
    path("users/drivers/", view=staff_member_required(all_drivers), name="all_drivers"),
    path("users/drivers/documents/filter", view=staff_member_required(filter_documents), name="filter_documents"),
    path("users/riders/", view=staff_member_required(all_riders), name="all_riders"),

    path("deactivate/driver/<str:username>/", view=staff_member_required(admin_deactivate_driver), name="deactivate_driver"),
    path("deactivate/rider/<str:username>/", view=staff_member_required(admin_deactivate_rider), name="deactivate_rider"),
    path("activate/admin/<str:username>/", view=staff_member_required(admin_switch), name="deactivate_admin"),
    path("users/session/<str:username>/end/", view=staff_member_required(admin_end_user_session), name="end-user_session"),

    path("add/rider/", view=staff_member_required(add_new_rider), name="add_rider"),
    path("add/driver/", view=staff_member_required(add_new_driver), name="add_driver"),
    path("add/administrator/", view=staff_member_required(add_new_admin), name="add_admin"),
]
