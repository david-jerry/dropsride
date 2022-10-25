from typing import Any

from django.shortcuts import redirect
from django.urls import reverse_lazy
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from django.conf import settings
from django.http import HttpRequest

from config.commons import send_auth_email

class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        send_auth_email(template_prefix=template_prefix, email=email, context=context)

    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def get_login_redirect_url(self, request):
        path = "/users/{username}/"
        return path.format(username=request.user.username)

    def get_email_confirmation_redirect_url(self, request):
        path = "/accounts/login/"
        return path

    # def save_user(self, request, user, form, commit=False):
    #     user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
    #     user.phone_number = form.cleaned_data.get('phone_number')
    #     user.gave_consent = True
        # user.save()


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def is_auto_signup_allowed(self, request, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
