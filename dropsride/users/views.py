from typing import Any, Dict
import urllib.parse

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.edit import FormMixin
from dropsride.settings.models import CarType

from dropsride.users.forms import UserSignupForm
from dropsride.users.mixins import LoginRequiredMixin, StaffRequiredMixin
from dropsride.users.models import SavedCards
from dropsride.utils.logger import LOGGER

User = get_user_model()


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client

    @property
    def callback_url(self):
        # use the same callback url as defined in your GitHub app, this url
        # must be absolute:
        return self.request.build_absolute_uri(reverse("facebook_callback"))

    # callback_url='http://localhost:8000/api/auth/facebook/login/callback/' if not settings.PRODUCTION else "https://dropsride.com/api/auth/facebook/login/callback/"


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

    @property
    def callback_url(self):
        # use the same callback url as defined in your GitHub app, this url
        # must be absolute:
        return self.request.build_absolute_uri(reverse("google_callback"))

    # callback_url = 'http://localhost:8000/api/auth/google/login/callback/' if not settings.PRODUCTION else "https://dropsride.com/api/auth/google/login/callback/"


def google_callback(request):
    params = urllib.parse.urlencode(request.GET)
    origin = (
        "http://localhost:8000/"
        if not settings.PRODUCTION
        else "https://dropsride.com/"
    )
    return redirect(f"{origin}api/auth/google/login/callback/?{params}")


def facebook_callback(request):
    params = urllib.parse.urlencode(request.GET)
    origin = (
        "http://localhost:8000/"
        if not settings.PRODUCTION
        else "https://dropsride.com/"
    )
    return redirect(f"{origin}api/auth/facebook/login/callback/?{params}")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    # def get_template_names(self):
    #     if not self.request.htmx:
    #         LOGGER.info("serving from request without htmx")
    #         return "users/user_detail.html"
    #     elif self.request.htmx:
    #         LOGGER.info("serving from request with htmx")
    #         return "admin/users/detail.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cartypes'] = CarType.objects.all()
        return context

user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    form_class = UserSignupForm
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class AllUsers(LoginRequiredMixin, FormMixin, ListView):
    model = User
    paginate_by = 10
    allow_empty = True
    context_object_name = "objects"
    page_kwarg = "page"
    template_name = "admin/users/list.html"
    form_class = UserSignupForm

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search and self.request.user.is_staff:
            query = User.objects.filter(
                Q(username__icontains=search)
                | Q(first_name__icontains=search)
                | Q(middle_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
            )
            return query
        elif not search and self.request.user.is_staff:
            query = User.objects.all()
            return query
        else:
            raise PermissionDenied()

    def get_template_names(self):
        if not self.request.htmx:
            LOGGER.info("serving from request without htmx")
            return "admin/users/list.html"
        elif self.request.htmx:
            LOGGER.info("serving from request with htmx")
            return "admin/users/snippets/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserSignupForm()
        return context


all_users = AllUsers.as_view()


# function views
def get_verified(request):
    object = request.user
    return render(
        request, "users/snippets/complete_process.html", context={"object": object}
    )


def get_profile_card(request):
    object = request.user
    return render(
        request, "users/snippets/profile_card.html", context={"object": object}
    )


def get_kin(request):
    object = request.user
    return render(request, "users/snippets/kin.html", context={"object": object})


def get_currency(request):
    object = request.user
    return render(
        request, "users/snippets/forms/currency.html", context={"object": object}
    )


def get_admin_detail(request, **kwargs):
    object = get_object_or_404(User, username=kwargs.get("username"))
    return render(request, "admin/users/detail.html", context={"object": object})


def get_detail(request):
    object = request.user
    return render(request, "users/snippets/detail.html", context={"object": object})

def get_vehicle(request):
    object = request.user
    return render(request, "users/snippets/forms/vehicle.html", context={"object": object})

def get_document(request):
    object = request.user
    return render(request, "users/snippets/forms/documents.html", context={"object": object})


def get_cards(request, pk):
    card = get_object_or_404(SavedCards, pk=pk, active=True)
    object = request.user
    return render(
        request, "users/snippets/card.html", context={"object": object, "card": card}
    )


def get_all_cards(request):
    object = request.user
    return render(
        request, "users/snippets/card_details.html", context={"object": object}
    )


def get_banks(request):
    object = request.user
    return render(request, "users/snippets/all_banks.html", context={"object": object})


def search_users(request):
    search = request.GET.get("search")
    if search:
        query = User.objects.filter(
            Q(username__icontains=search)
            | Q(first_name__icontains=search)
            | Q(middle_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
        )
        return render(request, "admin/users/list.html", context={"objects": query})
    else:
        query = User.objects.all()
        return render(request, "admin/users/list.html", context={"objects": query})
