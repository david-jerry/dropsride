from django.urls import path

from dropsride.settings.views import (
    car_types,
    car_types_detail,
    car_types_update,
    localization_detail,
    localization_list,
    localization_update,
)

app_name = "settings"
urlpatterns = [
    path("localization/", view=localization_list, name="localization_list"),
    path("localization/<uuid>/", view=localization_detail, name="localization_detail"),
    path(
        "localization/<uuid>/update/",
        view=localization_update,
        name="localization_update",
    ),
    path("cars/", view=car_types, name="car_types"),
    path("cars/table/", view=car_types_detail, name="car_detail"),
    path("cars/<slug>/update/", view=car_types_update, name="car_update"),
]
