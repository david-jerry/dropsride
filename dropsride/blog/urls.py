from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    detail_view,
    list_view,
    news_pages_detail,
    news_pages_list,
    update_view,
)

app_name = "news"
urlpatterns = [
    path("", news_pages_list, name="pages_list"),
    path("pages/<slug>/", news_pages_detail, name="pages_detail"),
    path("admin/", view=login_required(list_view), name="list"),
    path("admin/<slug>/update/", view=update_view, name="update"),
    path("admin/<slug>/", view=login_required(detail_view), name="detail"),
]
