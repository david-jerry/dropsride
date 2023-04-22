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
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    RedirectView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from dropsride.users.mixins import LoginRequiredMixin, StaffRequiredMixin
from dropsride.utils.logger import LOGGER

from .forms import ApplicantsForm, CareersForm, DepartmentForm
from .models import Applicants, Careers, Teams

User = get_user_model()


# Create your views here.
class CareerListView(StaffRequiredMixin, ListView):
    model = Careers
    template_name = "admin/careers/list.html"
    context_object_name = "objects"
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True
    queryset = Careers.published.all_careers()

    def get_queryset(self):
        search = self.request.GET.get("search") or "all"
        return Careers.published.search_careers(search)

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/careers/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/careers/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Teams.objects.all()
        return context


career_list = CareerListView.as_view()


class CareerPagesListView(ListView):
    model = Careers
    template_name = "careers/list.html"
    context_object_name = "objects"
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True
    queryset = Careers.published.all_published_careers()

    def get_queryset(self):
        search = self.request.GET.get("search") or "all"
        return Careers.published.search_careers(search)

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "careers/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "careers/snippets/career_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Teams.objects.all()
        return context


pages_career_list = CareerPagesListView.as_view()


class CareerDetailView(StaffRequiredMixin, DetailView):
    template_name = "careers/detail.html"
    model = Careers
    context_object_name = "object"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_template_names(self):
        if self.request.user.is_staff:
            return "admin/careers/detail.html"


career_detail = CareerDetailView.as_view()


def career_pages_detail(request, slug):
    object = get_object_or_404(Careers, slug=slug)
    context = {"object": object}
    return render(request, "careers/detail.html", context)


class CareerUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/careers/snippets/update.html"
    model = Careers
    form_class = CareersForm

    def get_object(self):
        return get_object_or_404(Careers, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()
        return context


career_update = CareerUpdateView.as_view()


class CareerCreateView(StaffRequiredMixin, CreateView):
    template_name = "admin/careers/snippets/create.html"
    model = Careers
    form_class = CareersForm


career_create = CareerCreateView.as_view()


def department_list(request):
    deps = Teams.objects.all()
    return render(
        request, "admin/careers/snippets/dep_list.html", context={"departments": deps}
    )


class DepartmentCreateView(StaffRequiredMixin, CreateView):
    template_name = "admin/careers/snippets/dep_create.html"
    model = Teams
    form_class = DepartmentForm


department_create = DepartmentCreateView.as_view()


class DepartmentUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/careers/snippets/dep_update.html"
    model = Teams
    form_class = DepartmentForm

    def get_object(self):
        return get_object_or_404(Teams, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()
        return context


department_update = CareerUpdateView.as_view()


class DepartmentDetailView(DetailView):
    template_name = "admin/careers/dep_detail.html"
    model = Teams
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_template_names(self):
        if self.request.user.is_staff:
            LOGGER.info("serving from request without htmx")
            return "admin/careers/dep_detail.html"
        elif not self.request.user.is_staff:
            LOGGER.info("serving from request without htmx")
            return "careers/dep_detail.html"


department_detail = DepartmentDetailView.as_view()


class ApplicantDetailView(StaffRequiredMixin, DetailView):
    template_name = "admin/careers/app_detail.html"
    model = Applicants
    pk_url_kwarg = "pk"
    query_pk_and_slug = True


applicant_detail = ApplicantDetailView.as_view()


class ApplicantCreateView(CreateView):
    template_name = "careers/snippets/app_create.html"
    model = Applicants
    form_class = ApplicantsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        context["object"] = Careers.objects.get(slug=slug)
        return context


applicant_create = ApplicantCreateView.as_view()
