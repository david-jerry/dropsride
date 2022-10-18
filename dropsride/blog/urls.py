from django.urls import path

from .views import (
    list_view,
    detail_view,
    create_view,
    update_view,
    delete_view,
)

app_name = "news"
urlpatterns = [
    path("", view=list_view, name="list"),
    path("create/", view=create_view, name="create"),
    path("<slug>/", view=detail_view, name="detail"),
    path("<slug>/update/", view=update_view, name="update"),
    path("<slug>/delete/", view=delete_view, name="delete"),
]
