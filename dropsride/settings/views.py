from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.edit import FormMixin

from dropsride.settings.forms import CartypeForm, LocalizationForm, PromoForm
from dropsride.settings.models import CarType, Localization, Promo
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


class PromoList(LoginRequiredMixin, FormMixin, ListView):
    model = Promo
    paginate_by = 10
    allow_empty = True
    context_object_name = "objects"
    page_kwarg = "page"
    template_name = "admin/promo/list.html"
    form_class = CartypeForm

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/promo/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/promo/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PromoForm()
        return context


promo_list = PromoList.as_view()


class PromoDetailView(StaffRequiredMixin, DetailView):
    template_name = "admin/promo/detail.html"
    model = Promo
    slug_field = "code"
    slug_url_kwarg = "code"


promos_detail = PromoDetailView.as_view()


class PromoUpdateView(StaffRequiredMixin, UpdateView):
    template_name = "admin/promo/snippets/update.html"
    model = Promo
    form_class = PromoForm
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_object(self):
        return get_object_or_404(Promo, code=self.args["code"])


promos_update = PromoUpdateView.as_view()


class PromoCreateView(StaffRequiredMixin, CreateView):
    template_name = "admin/promo/snippets/create.html"
    model = Promo
    form_class = PromoForm


promos_create = PromoCreateView.as_view()
