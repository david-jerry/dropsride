from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import FormMixin

from dropsride.settings.forms import CartypeForm, LocalizationForm
from dropsride.settings.models import CarType, Localization
from dropsride.users.mixins import LoginRequiredMixin, StaffRequiredMixin
from dropsride.utils.logger import LOGGER


# Create your views here.
class LocalizationList(LoginRequiredMixin, FormMixin, ListView):
    model = Localization
    paginate_by = 10
    allow_empty = True
    context_object_name = "objects"
    page_kwarg = "page"
    template_name = "admin/localization/list.html"
    form_class = LocalizationForm

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search and self.request.user.is_staff:
            query = Localization.objects.filter(
                Q(uuid__icontains=search) | Q(state__state__icontains=search)
            )
            return query
        elif not search and self.request.user.is_staff:
            query = Localization.objects.all()
            return query
        else:
            raise PermissionDenied()

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/localization/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/localization/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LocalizationForm()
        return context


localization_list = LocalizationList.as_view()


class LocalizationDetails(LoginRequiredMixin, DetailView):
    model = Localization
    template_name = "admin/localization/detail.html"
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


localization_detail = LocalizationDetails.as_view()


class LocalizationUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/localization/snippets/update.html"
    model = Localization
    form_class = LocalizationForm
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_object(self):
        return get_object_or_404(Localization, uuid=self.kwargs["uuid"])


localization_update = LocalizationUpdateView.as_view()


class CarTypeList(LoginRequiredMixin, FormMixin, ListView):
    model = CarType
    paginate_by = 10
    allow_empty = True
    context_object_name = "objects"
    page_kwarg = "page"
    template_name = "admin/cartype/list.html"
    form_class = CartypeForm

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/cartype/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/cartype/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CartypeForm()
        return context


car_types = CarTypeList.as_view()


def car_types_detail(request):
    cartypes = CarType.objects.all()
    return render(
        request, "admin/cartype/snippets/table.html", context={"objects": cartypes}
    )


class CarTypeUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/cartype/snippets/update.html"
    model = CarType
    form_class = CartypeForm
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self):
        return get_object_or_404(CarType, slug=self.kwargs["slug"])


car_types_update = CarTypeUpdateView.as_view()
