import datetime
import json
import requests

from django.urls import resolve
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.base import ContextMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from humanfriendly import format_timespan
from urllib.parse import urlencode

class HtmxResponseMixin(TemplateResponseMixin, ContextMixin):
    def get_template_names(self):
        app_name = resolve(self.request.path).app_name
        return [f"{app_name}/{self.template_name}"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context["base_template"] = "partial.html"
        else:
            context["base_template"] = "base.html"
        return context

class StaffRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(f'/accounts/login/?next={request.path}')
        return super().dispatch(request, *args, **kwargs)

class CompanyRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_company:
            return redirect(f'/accounts/login/?next={request.path}')
        return super().dispatch(request, *args, **kwargs)

class DriverRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_driver:
            return redirect(f'/accounts/login/?next={request.path}')
        return super().dispatch(request, *args, **kwargs)

class LoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f'/accounts/login/?next={request.path}')
        return super().dispatch(request, *args, **kwargs)

def reCAPTCHAValidation(token):
    """Validate google recaptcha 3 within a form

    Args:
        token (_type_): _description_
    """

    result = requests.post(
        'https://www.google.com/recaptcha/api/siteverify/',
        data={
            'secret': settings.GOOGLE_CAPTCHA_SITE_KEY,
            'response': token
        }
    )

    return result.json()

def RedirectParams(**kwargs):
    """used to append url parameters when redirecting
    """

    url = kwargs.get("url")
    params = kwargs.get("params")
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += "?" + query_string
    return response


class AxiosFormMixin(object):
    """Mixin to ajaxify django form errors

    Args:
        object (_type_): _description_
    """
    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST  or "__field_name__" in request.FILES:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })


def Directions(*args, **kwargs):
    """Handles google direction matrix from google api
    """

    pickup_lat = kwargs.get('pickup_lat')
    pickup_long = kwargs.get('pickup_long')
    waypointa_lat = kwargs.get('waypointa_lat')
    waypointa_long = kwargs.get('waypointa_long')
    waypointb_lat = kwargs.get('waypointb_lat')
    waypointb_long = kwargs.get('waypointb_long')
    waypointc_lat = kwargs.get('waypointc_lat')
    waypointc_long = kwargs.get('waypointc_long')
    waypointd_lat = kwargs.get('waypointd_lat')
    waypointd_long = kwargs.get('waypointd_long')
    destination_lat = kwargs.get('destination_lat')
    destination_long = kwargs.get('destination_long')

    origin = f"{pickup_lat},{pickup_long}"
    destination = f"{destination_lat},{destination_long}"
    waypoints = f"{waypointa_lat},{waypointa_long}|{waypointb_lat},{waypointb_long}|{waypointc_lat},{waypointc_long}|{waypointd_lat},{waypointd_long}"

    result = requests.get(
        'https://maps.googleapis.com/maps/api/directions/json?',
        params={
            'origin':origin,
            'destination':destination,
            'waypoints':waypoints,
            'key':settings.GOOGLE_API
        }
    )

    directions = result.json()

    if directions['status'] == 'OK':
        routes = directions["routes"][0]['legs']

        distance = 0
        duration = 0
        route_list = []

        for route in range(len(routes)):
            distance += int(routes[route]['distance']['values'])
            duration += int(routes[route]['duration']['values'])

            route_step = {
                'origin': routes[route]['start_address'],
                'destination': routes[route]['end_address'],
                'distance': routes[route]['distance']['text'],
                'duration': routes[route]['duration']['text'],

                'steps': [
                    [
                        s['distance']['text'],
                        s['duration']['text'],
                        s['html_instructions'],
                    ]
                    for s in routes[route]['steps']
                ]
            }
        route_list.append(route_step)
    return {
        'origin':origin,
        'destination':destination,
        'distance':f"{round(distance/1000, 2)} Km",
        'duration': format_timespan(duration),
        "route": route_list
    }
