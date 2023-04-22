from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from dropsride.transactions.models import Transaction
from dropsride.users.mixins import LoginRequiredMixin
from dropsride.utils.logger import LOGGER


# Create your views here.
class TransactionList(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transactions/list.html"
    paginate_by = 10
    allow_empty = True
    context_object_name = "objects"
    page_kwarg = "page"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            if user.user_transaction:
                return user.user_transaction.all()
            return []
        else:
            return redirect(reverse("/accounts/login/?next=/users/transactions/"))

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "transactions/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "transactions/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.request.user
        return context


transactions = TransactionList.as_view()


class TransactionDetail(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = "transactions/detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self):
        object = get_object_or_404(
            Transaction, slug=self.kwargs.get("slug"), owner=self.request.user
        )
        return object


transactions_detail = TransactionDetail.as_view()
