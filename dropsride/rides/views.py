from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from dropsride.rides.models import Trips
from dropsride.settings.models import CarType
from dropsride.users.mixins import LoginRequiredMixin
from dropsride.utils.logger import LOGGER


# Create your views here.
class TripsList(LoginRequiredMixin, ListView):
    model = Trips
    template_name = "rides/list.html"
    context_object_name = "objects"
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True
    queryset = Trips.objects.all()

    def get_queryset(self):
        # if self.request.user.is_driver and self.request.user.on_a_ride and self.request.user.is_authenticated and Trips.objects.filter(driver=self.request.user, active=True).exists():
        #     return Trips.objects.get(driver=self.request.user, active=True)
        # elif not self.request.user.is_driver and self.request.user.on_a_ride and self.request.user.is_authenticated and Trips.objects.filter(user=self.request.user, active=True).exists():
        #     return Trips.objects.get(user=self.request.user, active=True)
        if self.request.user.is_driver and self.request.user.is_authenticated:
            return self.request.user.trip_driver.all()
        elif not self.request.user.is_driver and self.request.user.is_authenticated:
            return self.request.user.rider_trip.all()

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "rides/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "rides/snippets/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = CarType.objects.all()

        return context


trips_list = TripsList.as_view()


class GetCarTypes(LoginRequiredMixin, UpdateView):
    model = Trips
    template_name = "rides/snippets/car_types.html"
    fields = [
        "state",
        "pickup",
        "p_point",
        "dropoff",
        "d_point",
        "pay_method",
        "car_type",
        "waypoint1_address",
        "waypoint1_point",
        "waypoint2_address",
        "waypoint2_point",
    ]

    def get_object(self):
        obj = get_object_or_404(Trips, uuid=self.kwargs["uuid"])
        if not self.request.user == obj.user:
            return PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = CarType.objects.all()
        context["object"] = self.get_object()
        return context


get_car_types = GetCarTypes.as_view()


class AdminTripsList(LoginRequiredMixin, ListView):
    model = Trips
    template_name = "rides/admin_list.html"
    context_object_name = "objects"
    page_kwarg = "page"
    paginate_by = 20
    allow_empty = True
    queryset = Trips.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff and self.request.user.is_authenticated:
            return Trips.objects.all()
        else:
            raise PermissionDenied()

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "rides/admin_list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "rides/snippets/admin_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['departments'] = Teams.objects.all()
        return context


admin_trips_list = AdminTripsList.as_view()


class TripsDetails(LoginRequiredMixin, DetailView):
    model = Trips
    slug_field = "uuid"
    slug_url_kwarg = "uuid"


trips_detail = TripsDetails.as_view()
