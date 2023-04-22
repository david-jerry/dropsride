from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    RedirectView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from taggit.models import Tag

from dropsride.users.mixins import LoginRequiredMixin, StaffRequiredMixin
from dropsride.utils.logger import LOGGER

from .forms import NewsForm
from .models import News

User = get_user_model()


# page to be requested for htmx loading of a detail page
def news_pages_detail(request, slug):
    object = get_object_or_404(News, slug=slug)
    context = {"object": object}
    return render(request, "news/detail.html", context)


class NewsPagesListView(ListView):
    model = News
    context_object_name = "objects"
    template_name = "news/list.html"
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True

    def get_queryset(self):
        search = self.request.GET.get("search") or "all"
        return News.published.search_published_posts(search)

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "news/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "news/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = (
            News.tags.all() or []
        )  # list(News.objects.all().values_list('tags__name', flat=True))
        context["recent_posts"] = News.published.get_recent_posts()
        context["featured_post"] = News.published.get_featured_posts()
        context["related_post"] = News.published.get_related_posts(
            news=self.get_object()
        )
        return context


news_pages_list = NewsPagesListView.as_view()


# Create your views here.
class NewsListView(FormMixin, StaffRequiredMixin, ListView):
    model = News
    template_name = "admin/news/list.html"
    context_object_name = "objects"
    form_class = NewsForm
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True
    queryset = News.published.all_posts()

    def get_queryset(self):
        search = self.request.GET.get("search") or "all"
        return News.published.search_posts(search)

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/news/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/news/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context["tags"] = (
            News.tags.all() or []
        )  # list(News.objects.all().values_list('tags__name', flat=True))
        context["recent_posts"] = News.published.get_recent_admin_posts()
        return context


list_view = NewsListView.as_view()


class NewsDetailView(StaffRequiredMixin, DetailView):
    template_name = "admin/news/detail.html"
    model = News
    context_object_name = "object"
    slug_field = "slug"
    slug_url_kwarg = "slug"


detail_view = NewsDetailView.as_view()


class NewsUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/news/snippets/update.html"
    model = News
    form_class = NewsForm

    def get_object(self):
        return get_object_or_404(News, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()
        return context


update_view = NewsUpdateView.as_view()
