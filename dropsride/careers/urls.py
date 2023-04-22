from django.urls import path

from .views import (
    applicant_create,
    applicant_detail,
    career_create,
    career_detail,
    career_list,
    career_pages_detail,
    career_update,
    department_create,
    department_detail,
    department_list,
    department_update,
    pages_career_list,
)

app_name = "careers"
urlpatterns = [
    path("departments/", view=department_list, name="department_list"),
    path("department/create/", view=department_create, name="department_create"),
    path("department/<slug>/update/", view=department_update, name="department_update"),
    path("department/<slug>/", view=department_detail, name="department_detail"),
    path("applicant/<pk>/", view=applicant_detail, name="applicant_detail"),
    path("applicant/<slug>/create/", view=applicant_create, name="applicant_create"),
    path("", view=career_list, name="list"),
    path("pages/", view=pages_career_list, name="pages_list"),
    path("create/", view=career_create, name="create"),
    path("pages/<slug>/", view=career_pages_detail, name="pages_detail"),
    path("<slug>/", view=career_detail, name="detail"),
    path("<slug>/update/", view=career_update, name="update"),
]
