import pprint
from urllib.parse import urlencode

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from humanfriendly import format_timespan

from dropsride.utils.logger import LOGGER


def phoneVerify(number):
    """Phone validation api from youverify

    Args:
        number (_type_): _description_
    """
    url = str(f"{settings.YOUVERIFY_ENV}/v2/api/identity/ng/phone")
    headers = {
        "token": str(settings.YOUVERIFY_API),
    }
    params = {
        "mobile": number,
        "isSubjectConsent": True,
    }

    res = requests.request("POST", url, headers=headers, params=params)
    res = res.json()
    pp = pprint.PrettyPrinter(indent=4)
    LOGGER.info(pp.pprint(res))
    LOGGER.info("Number Verification Done")
    return res


def bvnVerify(bvn, fn, ln, dob):
    """BVN validation api from youverify

    Args:
        number (_type_): _description_
    """
    url = str(f"{settings.YOUVERIFY_ENV}/v2/api/identity/ng/bvn")
    headers = {
        "token": str(settings.YOUVERIFY_API),
    }
    params = {
        "id": bvn,
        "isSubjectConsent": True,
        "validations": {
            "data": {
                "lastName": fn,
                "firstName": ln,
                "dateOfBirth": dob,
            }
        },
    }

    res = requests.request("POST", url, headers=headers, params=params)
    res = res.json()
    pp = pprint.PrettyPrinter(indent=4)
    LOGGER.info(pp.pprint(res))
    LOGGER.info("BVN Verification Done")
    return res


def ninVerify(nin, fn, ln):
    """NIN validation api from youverify

    Args:
        number (_type_): _description_
    """
    url = str(f"{settings.YOUVERIFY_ENV}/v2/api/identity/ng/vnin")
    headers = {
        "token": str(settings.YOUVERIFY_API),
    }
    params = {
        "id": nin,
        "isSubjectConsent": True,
        "validations": {
            "data": {
                "lastName": ln,
                "firstName": fn,
            }
        },
    }

    res = requests.request("POST", url, headers=headers, params=params)
    res = res.json()
    pp = pprint.PrettyPrinter(indent=4)
    LOGGER.info(pp.pprint(res))
    LOGGER.info("NIN Verification Done")
    return res


def accVerify(number, bankCode):
    """Verify that a given bank account number is owned by a user

    Args:
        number (String): Users account number
        bankCode (String): Registered bank code on the platform
    """

    url = str(
        f"{settings.YOUVERIFY_ENV}/v2/api/identity/ng/bank-account-number/resolve"
    )
    headers = {
        "token": str(settings.YOUVERIFY_API),
    }
    params = {
        "accountNumber": number,
        "bankCode": bankCode,
        "isSubjectConsent": True,
    }

    res = requests.request("POST", url, headers=headers, params=params)
    res = res.json()
    pp = pprint.PrettyPrinter(indent=4)
    LOGGER.info(pp.pprint(res))
    LOGGER.info("NIN Verification Done")
    return res


def driverLicenseVerify(license, fn, ln, dob):
    """Driver License validation api from youverify

    Args:
        number (_type_): _description_
    """
    url = str(f"{settings.YOUVERIFY_ENV}/v2/api/identity/ng/drivers-license")
    headers = {
        "token": str(settings.YOUVERIFY_API),
    }
    params = {
        "id": license,
        "isSubjectConsent": True,
        "validations": {
            "data": {
                "lastName": ln,
                "firstName": fn,
                "dateOfBirth": dob,
            }
        },
    }

    res = requests.request("POST", url, headers=headers, params=params)
    res = res.json()
    pp = pprint.PrettyPrinter(indent=4)
    LOGGER.info(pp.pprint(res))
    LOGGER.info("License Verification Done")
    return res


def reCaptchaValidation(token):
    """reCAPTCHA validation"""
    result = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": settings.RECAPTCHA_PRIVATE_KEY, "response": token},
    )

    res = result.json()
    return res


def RedirectParams(**kwargs):
    """
    Used to append url parameters when redirecting users
    """
    url = kwargs.get("url")
    params = kwargs.get("params")
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response["Location"] += "?" + query_string
    return response


def Directions(*args, **kwargs):
    """
    Handles directions from Google
    """

    lat_a = kwargs.get("lat_a")
    long_a = kwargs.get("long_a")
    lat_b = kwargs.get("lat_b")
    long_b = kwargs.get("long_b")
    lat_c = kwargs.get("lat_c")
    long_c = kwargs.get("long_c")
    lat_d = kwargs.get("lat_d")
    long_d = kwargs.get("long_d")

    origin = f"{lat_a},{long_a}"
    destination = f"{lat_b},{long_b}"
    waypoints = f"{lat_c},{long_c}|{lat_d},{long_d}"

    result = requests.get(
        "https://maps.googleapis.com/maps/api/directions/json?",
        params={
            "origin": origin,
            "destination": destination,
            "waypoints": waypoints,
            "key": settings.GOOGLE_API_KEY,
        },
    )

    directions = result.json()

    if directions["status"] == "OK":
        routes = directions["routes"][0]["legs"]

        distance = 0
        duration = 0
        route_list = []

        for route in range(len(routes)):
            distance += int(routes[route]["distance"]["value"])
            duration += int(routes[route]["duration"]["value"])

            route_step = {
                "origin": routes[route]["start_address"],
                "destination": routes[route]["end_address"],
                "distance": routes[route]["distance"]["text"],
                "duration": routes[route]["duration"]["text"],
                "steps": [
                    [
                        s["distance"]["text"],
                        s["duration"]["text"],
                        s["html_instructions"],
                    ]
                    for s in routes[route]["steps"]
                ],
            }

            route_list.append(route_step)

    return {
        "origin": origin,
        "destination": destination,
        "distance": f"{round(distance/1000, 2)} Km",
        "duration": format_timespan(duration),
        "route": route_list,
    }


def FormErrors(*args):
    """
    Handles form error that are passed back to AJAX calls
    """
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message


class AxiosFormMixin:

    """
    Mixin to ajaxify django form - can be over written in view by calling form_valid method
    """

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request, self.form_class)
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            message = FormErrors(form)
            return JsonResponse({"result": "Error", "message": message})
        return response

    def validate_field(self, request, form):
        field_name = request.POST.get("__field_name__")
        form = form(request.POST)
        form.is_valid()
        return JsonResponse(
            status=203,
            data={
                "errors": form.errors.get(field_name, []),
            },
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            form.save()
            return JsonResponse({"result": "Success", "message": ""})
        return response
