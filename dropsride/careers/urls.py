from django.urls import path

from .views import (
    list_view,
    create_view,
    detail_view,
    delete_view,
    create_department_view,
    department_detail_view,
    applicant_detail_view,
)

app_name = "careers"
urlpatterns = [
    path("", view=list_view, name="list"),
    path("department/<slug>/", view=department_detail_view, name="department_detail"),
    path("applicant/<slug>/", view=applicant_detail_view, name="applicant_detail"),
    path("create/", view=create_view, name="create"),
    path("create/department/", view=create_department_view, name="create_department"),
    path("<slug>/", view=detail_view, name="detail"),
    path("<slug>/delete/", view=delete_view, name="delete"),
]
