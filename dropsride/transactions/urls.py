from django.urls import path

from dropsride.transactions.views import transactions, transactions_detail

app_name = "transactions"
urlpatterns = [
    path("", view=transactions, name="list"),
    path("<slug>/detail/", view=transactions_detail, name="details"),
]
