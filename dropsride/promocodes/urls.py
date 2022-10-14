from django.urls import path
from django.views.generic import TemplateView

from .views import (
    filter_coupons,
    create_coupons,
    update_coupons,
    delete_coupons
)

app_name = "coupons"
urlpatterns = [
    path("", view=TemplateView.as_view(template_name="coupons/list.html"), name="list"),
    path("json/", view=filter_coupons, name="coupons-json"),
    path("create/", view=create_coupons, name="coupons-create"),
    path("update/<int:pk>/", view=update_coupons, name="coupons-update"),
    path("delete/<int:pk>/", view=delete_coupons, name="coupons-delete"),
]
