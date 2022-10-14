from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
    CreateView,
    ListView,
)
from django.http import JsonResponse
from dropsride.admins.models import Admins

from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.documents.models import Documents
from dropsride.sitesettings.models import (
    DriverSettings,
    Localization,
    VehicleType,
)

User = get_user_model()

# Create your views here.
@login_required
def admin_dashboard(request):
    context = {}
    return render(request, "admins/dashboard.html", context)


# -------------------------------------------------------------------------------#
# admin settings views
# -------------------------------------------------------------------------------#
@login_required
def CreateDriversConfigSettings(request):
    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    drv_set = (
        DriverSettings.objects.first()
        if DriverSettings.objects.first().exists()
        else None
    )

    context = {
        "object": drv_set,
    }

    if request.method != "POST":
        approved_waiting_time = request.POST.get("approved_waiting_time")
        driver_search_radius = request.POST.get("driver_search_radius")
        DriverSettings.objects.create(
            approved_waiting_time=int(approved_waiting_time),
            driver_search_radius=int(driver_search_radius),
        )
        return JsonResponse(
            {"status": 201, "message": "Created Drivers Default Configuration"}
        )
    return render(request, "admin/driver-config.html", context)


@login_required
def UpdateDriversConfigSettings(request, pk):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    drv_set = get_object_or_404(Drivers, pk=pk)

    context = {
        "object": drv_set,
    }

    if request.method != "PUT":
        approved_waiting_time = request.POST.get("approved_waiting_time")
        driver_search_radius = request.POST.get("driver_search_radius")
        DriverSettings.objects.filter(pk=pk).update(
            approved_waiting_time=int(approved_waiting_time),
            driver_search_radius=int(driver_search_radius),
        )
        return JsonResponse(
            {"status": 200, "message": "Updated Drivers Default Configuration"}
        )
    return render(request, "admin/driver-config.html", context)




# Vehicle Type Settings
# ------------------------------------------------------------------------------
@login_required
def filter_vehicles(request):
    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

    vehicles = VehicleType.objects.values()
    vehicle_list = list(vehicles)
    return JsonResponse(vehicle_list, safe=False)


def CreateVehicleConfigSettings(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method != "POST":
        v_type = request.POST.get("v_type")
        v_status = request.POST.get("v_status")
        percentage = request.POST.get("percentage")
        default_rate_by_state = request.POST.get("default_rate_by_state")
        cost_per_km = request.POST.get("cost_per_km")
        base_unit = request.POST.get("base_unit")
        max_seater = request.POST.get("max_seater")
        max_luggage = request.POST.get("max_luggage")

        VehicleType.objects.create(
            v_type = v_type,
            v_status = v_status,
            percentage = percentage,
            default_rate_by_state = default_rate_by_state,
            cost_per_km = cost_per_km,
            base_unit = base_unit,
            max_seater = int(max_seater),
            max_luggage = int(max_luggage),
        )
        return JsonResponse(
            {"status": 201, "message": "Created Global Settings for Vehicle Types"}
        )
    return render(request, "admin/vehicle-config.html")


@login_required
def UpdateVehicleConfigSettings(request, pk):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    drv_set = get_object_or_404(VehicleType, pk=pk)

    context = {
        "object": drv_set,
    }

    if request.method != "PUT":
        v_type = request.POST.get("v_type")
        v_status = request.POST.get("v_status")
        percentage = request.POST.get("percentage")
        default_rate_by_state = request.POST.get("default_rate_by_state")
        cost_per_km = request.POST.get("cost_per_km")
        base_unit = request.POST.get("base_unit")
        max_seater = request.POST.get("max_seater")
        max_luggage = request.POST.get("max_luggage")
        VehicleType.objects.filter(pk=pk).update(
            v_type = v_type,
            v_status = v_status,
            percentage = percentage,
            default_rate_by_state = default_rate_by_state,
            cost_per_km = cost_per_km,
            base_unit = base_unit,
            max_seater = int(max_seater),
            max_luggage = int(max_luggage),
        )
        return JsonResponse(
            {"status": 200, "message": "Updated Global Vehicle Configuration"}
        )
    return render(request, "admin/vehicle-config.html", context)



# Localization Settings
# ______________________________________________________________________________
@login_required
def filter_localizations(request):
    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

    ocalizations = Localization.objects.values()
    local_list = list(ocalizations)
    return JsonResponse(local_list, safe=False)


@login_required
def CreateLocalizationConfigSettings(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        if not Localization.objects.filter(state=state).exists():
            state = request.POST.get("state")
            amount = request.POST.get("amount")
            Localization.objects.create(
                state=state,
                amount=int(amount),
            )
            return JsonResponse(
                {"status": 201, "message": "Created New Localization Configuration"}
            )
        else:
            return JsonResponse(
                {"status": 400, "message": "Localizaion already exists"}
            )
    return render(request, "admin/localization-config.html")


@login_required
def UpdateLocalizationConfigSettings(request, pk):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    drv_set = get_object_or_404(Localization, pk=pk)

    context = {
        "object": drv_set,
    }

    if request.method == "PUT":
        if Localization.objects.filter(pk=pk).exists():
            state = request.POST.get("state")
            amount = request.POST.get("amount")
            Localization.objects.create(
                state=state,
                amount=int(amount),
            )
            return JsonResponse(
                {"status": 201, "message": "Updated Localization Configuration"}
            )
        else:
            return JsonResponse(
                {"status": 400, "message": "Localizaion Does not exists"}
            )
    return render(request, "admin/localization-config.html", context=context)

# -------------------------------------------------------------------------------#
# end admin settings views
# -------------------------------------------------------------------------------#






# -------------------------------------------------------------------------------#
# admin documents views
# -------------------------------------------------------------------------------#
@login_required
def filter_documents(request):
    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

    documents = Documents.objects.values()
    documents_list = list(documents)
    return JsonResponse(documents_list, safe=False)


@login_required
def approve_documents(request, pk):
    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

    try:
        Documents.objects.get(pk=pk).delete()
    except Documents.DoesNotExist:
        return JsonResponse(
            {"status": 400, "message": f"Document with {pk} does not exist"}
        )


# -------------------------------------------------------------------------------#
# end admin documents views
# -------------------------------------------------------------------------------#






# -------------------------------------------------------------------------------#
# admin list drivers, users and riders
# -------------------------------------------------------------------------------#
class AllUsers(LoginRequiredMixin, ListView):
    model = User
    template_name = "admins/users.html"
    queryset = User.objects.all()
    context_object_name = "users"
    allow_empty = True
    page_kwarg = "page"
    paginate_by = 50


all_users = AllUsers.as_view()


class AllDrivers(LoginRequiredMixin, ListView):
    model = Drivers
    template_name = "admins/drivers.html"
    queryset = Drivers.objects.all()
    context_object_name = "drivers"
    allow_empty = True
    page_kwarg = "page"
    paginate_by = 50


all_drivers = AllDrivers.as_view()


class AllRiders(LoginRequiredMixin, ListView):
    model = Drivers
    template_name = "admins/riders.html"
    queryset = Riders.objects.all()
    context_object_name = "riders"
    allow_empty = True
    page_kwarg = "page"
    paginate_by = 50


all_riders = AllRiders.as_view()
# -------------------------------------------------------------------------------#
# end admin list drivers, users and riders
# -------------------------------------------------------------------------------#





# -------------------------------------------------------------------------------#
# admin add new drivers and admins
# -------------------------------------------------------------------------------#
def add_new_driver(request):
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    phone_number = request.POST.get("phone_number")
    gender = request.POST.get("gender")
    date_of_birth = request.POST.get("date_of_birth")
    country = request.POST.get("country")
    image = request.POST.get("image")

    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        if (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != "" or (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != None:
            User.objects.create(
                email=email,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                username=username,
                phone_number=phone_number,
                gender=gender,
                date_of_birth=date_of_birth,
                country=country,
                image=image,
                is_driver=True,
                gave_consent=True,
                password=email,
            )
            return JsonResponse(
                {"status": 201, "message": "Driver Created Successfully"}
            )
        else:
            return JsonResponse({"status": 204, "message": "No Content to process"})
    return render(request, "admins/add-driver.html")


def add_new_admin(request):
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    phone_number = request.POST.get("phone_number")
    gender = request.POST.get("gender")
    date_of_birth = request.POST.get("date_of_birth")
    country = request.POST.get("country")
    image = request.POST.get("image")

    if not request.user.is_superuser:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        if (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != "" or (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != None:
            User.objects.create(
                email=email,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                username=username,
                phone_number=phone_number,
                gender=gender,
                date_of_birth=date_of_birth,
                country=country,
                image=image,
                is_driver=True,
                gave_consent=True,
                is_superuser=True,
                password=email,
            )
            return JsonResponse(
                {"status": 201, "message": "Admin Created Successfully"}
            )
        else:
            return JsonResponse({"status": 204, "message": "No Content to process"})
    return render(request, "admins/add-admin.html")


def add_new_rider(request):
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    phone_number = request.POST.get("phone_number")
    gender = request.POST.get("gender")
    date_of_birth = request.POST.get("date_of_birth")
    country = request.POST.get("country")
    image = request.POST.get("image")

    if not request.user.is_staff:
        return JsonResponse(
            {
                "status": 401,
                "message": "Unauthorized Access Denied: You are not a staff",
            }
        )

    if request.method == "POST":
        if (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != "" or (
            email,
            first_name,
            middle_name,
            last_name,
            username,
            phone_number,
            gender,
            date_of_birth,
            country,
            image,
        ) != None:
            User.objects.create(
                email=email,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                username=username,
                phone_number=phone_number,
                gender=gender,
                date_of_birth=date_of_birth,
                country=country,
                image=image,
                is_driver=False,
                gave_consent=True,
                is_superuser=True,
                password=email,
            )
            return JsonResponse(
                {"status": 201, "message": "Rider Created Successfully"}
            )
        else:
            return JsonResponse({"status": 204, "message": "No Content to process"})
    return render(request, "admins/add-rider.html")


# -------------------------------------------------------------------------------#
# end admin add new drivers and admins
# -------------------------------------------------------------------------------#


# -------------------------------------------------------------------------------#
# admin switches for drivers, riders and admins
# -------------------------------------------------------------------------------#
@login_required
def admin_switch(request, username):
    if request.method == "POST":
        switched = request.POST.get("switched")
        if switched == "on":
            User.objects.filter(username=username).update(is_superuser=True)
            return JsonResponse(
                {
                    "status": 200,
                    "message": f"Switched on Administrator Access for {username}",
                }
            )
        else:
            User.objects.filter(username=username).update(is_superuser=False)
            return JsonResponse(
                {
                    "status": 200,
                    "message": f"Switched off Administrtor Access for {username}",
                }
            )


@login_required
def admin_deactivate_driver(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        switched = request.POST.get("switched")
        if switched == "on":
            Drivers.objects.filter(user=user).update(approved=True)
            return JsonResponse(
                {"status": 200, "message": f"Deactivation is on for Driver: {username}"}
            )
        else:
            Drivers.objects.filter(user=user).update(approved=False)
            return JsonResponse(
                {
                    "status": 200,
                    "message": f"Deactivation is off for Driver: {username}",
                }
            )


@login_required
def admin_deactivate_rider(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        switched = request.POST.get("switched")
        if switched == "on":
            Riders.objects.filter(user=user).update(approved=True)
            return JsonResponse(
                {"status": 200, "message": f"Deactivation is on for Rider: {username}"}
            )
        else:
            Riders.objects.filter(user=user).update(approved=False)
            return JsonResponse(
                {"status": 200, "message": f"Deactivation is off for Rider: {username}"}
            )


@login_required
def admin_end_user_session(request, username):
    user = get_object_or_404(User, username=username)
    for s in Session.objects.all():
        data = s.get_decoded()
        if data.get("auth_user_id", None) == user.id:
            s.delete()
            return JsonResponse(
                {
                    "status": 200,
                    "message": f"Successfully Ended {user.username.title()} Session",
                }
            )
        else:
            return JsonResponse(
                {
                    "status": 400,
                    "message": f"{user.username.title()} Session Unavailable",
                }
            )


# -------------------------------------------------------------------------------#
# end admin switches for drivers, riders and admins
# -------------------------------------------------------------------------------#
