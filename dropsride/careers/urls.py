from django.urls import path

from .views import (
    list_view,
    create_view,
    detail_view,
    delete_view,
    create_department_view,
)

app_name = "careers"
urlpatterns = [
    path("", view=list_view, name="list"),
    path("create/", view=create_view, name="create"),
    path("create/department/", view=create_department_view, name="create_department"),
    path("<slug>/", view=detail_view, name="detail"),
    path("<slug>/delete/", view=delete_view, name="delete"),
]
