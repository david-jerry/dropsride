from django.urls import path

from dropsride.rides.views import (
    admin_trips_list,
    get_car_types,
    trips_detail,
    trips_list,
)

app_name = "trips"
urlpatterns = [
    path("", view=trips_list, name="list"),
    path("admin/list/", view=admin_trips_list, name="admin_list"),
    path("<uuid>/", view=trips_detail, name="detail"),
    path("<uuid>/update/", view=get_car_types, name="update"),
]
