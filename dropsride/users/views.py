import datetime
from asgiref.sync import sync_to_async
import httpx
import asyncio
from config.commons import send_html_mail, signup_users
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from config.mixins import LoginRequiredMixin
from config.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, ListView, FormView, DeleteView
from django.http import JsonResponse
from django.utils import timezone

# from allauth import app_settings
from allauth.account import app_settings, signals
from allauth.account.adapter import get_adapter
from allauth.account.forms import *
from allauth.account.views import SignupView, PasswordResetFromKeyView, LoginView, ConfirmEmailView, PasswordChangeView, PasswordResetView, PasswordSetView
from allauth.account.utils import complete_signup, logout_on_password_change, perform_login
from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from allauth import ratelimit

from paystackapi.paystack import Paystack
from paystackapi.verification import Verification

from messente_api import OmnimessageApi, SMS, Omnimessage, Configuration, ApiClient
from messente_api.rest import ApiException

from dropsride.companies.models import Company
from dropsride.utils.logger import LOGGER
from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.users.models import BankAccount, SavedCards, UserNextOfKin, UserSocialAccounts, VerifiedPhone
from dropsride.users.forms import AddBankAccountForm, AddCardForm, AddNextOfKin, CompanySignupForm, DriverSignupForm, UpdateCardForm, UserAddressForm, UserLoginForm, UserSignupForm, UserUpdateForm, UserUpdateImageForm, UserUpdateSocialAccounts, ValidatePhoneForm
from dropsride.utils.unique_generators import random_code_generator
from django.templatetags.static import static

from webpush import send_user_notification, send_group_notification

User = get_user_model()
paystack = Paystack(secret_key=settings.PAYSTACK_TEST_SK)


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

def time_out_phone_verification(instance):
    """If the verification code has stayed more than 5 mins generate a new
    verification code and send it to the users line. then have them revalidate

    Args:
        instance (_type_): _description_

    Returns:
        _type_: _description_
    """
    # five_min = instance.modified > instance.endtime
    if timezone.now() > instance.endtime:
        VerifiedPhone.objects.filter(user=instance.user, code=instance.code, verified=False).update(code=random_code_generator(instance))
        # instance.code = random_code_generator(instance)
        configuration = Configuration()
        configuration.username = settings.MESSENTE_API_USERNAME
        configuration.password = settings.MESSENTE_API_PASSWORD

        api_instance = OmnimessageApi(ApiClient(configuration))

        sms = SMS(sender="+2347069916149", text=f"The verification code had expired. \nPlease verify within 5 mins time to avoid code expiration again.\n\nYour new code is: {instance.code}")

        omnimessage = Omnimessage(messages=tuple([sms]), to=instance.user.phone_number)

        domain = "https://www.dropsride.com" if settings.PRODUCTION else "http://localhost:8000"
        link = reverse("sms_verify", kwargs={"code":instance.code, "user":instance.user})

        msg = f"""
        Dear {instance.user.username.title()},
        <br>
        <br>
        Your previous verification code expired.<br>
        please find attached your new verification code: {instance.code}
        <br>
        You can also verify by clicking the link below\n\n{domain}{link}
        <br>
        """
        send_html_mail(subject=f"PHONE VERIFICATION CODE", html_content=msg, from_email="DROPS TECHNOLOGY LIMITED <noreply@dropsride.com>", recipient_list=[instance.user.email])


        try:
            response = api_instance.send_omnimessage(omnimessage)
            LOGGER.info(
                "[PHONE VERIFICATION SUCCESS] Successfully sent Omnimessage with id: %s that consists of the following messages:"
                % response.omnimessage_id
            )
            for message in response.messages:
                LOGGER.info(message)
            pass
        except ApiException as exception:
            LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)
            pass
    pass

def sms_verification_link(request, code, user):
    """sends the verification code via a link through the sms

    Args:
        request (_type_): http request
        code (_type_): code from the sms link

    Returns:
        _type_: _description_
    """
    usr = get_object_or_404(User, username=user)
    LOGGER.info(usr)
    if VerifiedPhone.objects.filter(code=code, user=usr.id, verified=False).exists():
        instance = VerifiedPhone.objects.get(code=code, user=usr, verified=False) or get_object_or_404(VerifiedPhone, code=code)
        # five_min = instance.time + timedelta(minutes=5)
        if timezone.now() > instance.endtime:
            fmins = datetime.datetime.now() + datetime.timedelta(minutes=5)
            new_code = random_code_generator(instance)
            VerifiedPhone.objects.filter(user=instance.user, code=instance.code, verified=False).update(code=new_code, endtime=fmins)
            # instance.code = random_code_generator(instance)
            configuration = Configuration()
            configuration.username = settings.MESSENTE_API_USERNAME
            configuration.password = settings.MESSENTE_API_PASSWORD

            api_instance = OmnimessageApi(ApiClient(configuration))

            sms = SMS(sender="+2347069916149", text=f"The verification code had expired. \nPlease verify within 5 mins time to avoid code expiration again.\n\nYour new code is: {new_code}")

            omnimessage = Omnimessage(messages=tuple([sms]), to=instance.user.phone_number)

            domain = "https://www.dropsride.com" if settings.PRODUCTION else "http://localhost:8000"
            link = reverse("sms_verify", kwargs={"code":new_code, "user":instance.user})

            msg = f"""
            Dear {instance.user.username.title()},
            <br>
            <br>
            Your previous verification code expired.<br>
            please find attached your new verification code: {new_code}
            <br>
            You can also verify by clicking the link below\n\n{domain}{link}
            <br>
            """
            send_html_mail(subject=f"PHONE VERIFICATION CODE", html_content=msg, from_email="DROPS TECHNOLOGY LIMITED <noreply@dropsride.com>", recipient_list=[instance.user.email])


            try:
                response = api_instance.send_omnimessage(omnimessage)
                LOGGER.info(
                    "[PHONE VERIFICATION SMS SENT SUCCESSFULLY] Successfully sent Omnimessage with id: %s that consists of the following messages:"
                    % response.omnimessage_id
                )
                for message in response.messages:
                    LOGGER.info(message)
                return redirect(reverse_lazy('users:verify_phone'))
            except ApiException as exception:
                LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)
                return redirect(reverse_lazy('account_login'))
        else:
            VerifiedPhone.objects.filter(code=code, user=usr, verified=False).update(verified=True, verified_code=code)
            LOGGER.info("[PHONE VERIFIED SUCCESSFULLY] The code has been used")
            return redirect(reverse_lazy('account_login'))
    else:
        return redirect(reverse_lazy('account_login'))

def request_new_code(request):
    user = get_object_or_404(User, username=request.user.username)
    instance = VerifiedPhone.objects.get(user=user, verified=False)
    new_code = random_code_generator(instance)
    instance.code = new_code
    instance.time = datetime.datetime.now()
    instance.endtime = datetime.datetime.now() + datetime.timedelta(minutes=5)
    instance.save()
    configuration = Configuration()
    configuration.username = settings.MESSENTE_API_USERNAME
    configuration.password = settings.MESSENTE_API_PASSWORD
    domain = "https://www.dropsride.com" if settings.PRODUCTION else "https://localhost:8000"
    link = reverse("sms_verify", kwargs={"code":new_code, "user":user})

    api_instance = OmnimessageApi(ApiClient(configuration))

    sms = SMS(sender="+2347069916149", text=f"please find attached your verification code: {instance.code}\n\nYou can also verify by clicking the link below\n\n{domain}{link}")
    # phone_number = User.objects.get(phone_number=instance.user.phone_number)
    omnimessage = Omnimessage(messages=tuple([sms]), to=user.phone_number)
    msg = f"""
    Dear {user.username.title()},
    <br>
    <br>
    please find attached your verification code: {new_code}
    <br>
    You can also verify by clicking the link below\n\n{domain}{link}
    <br>
    """
    send_html_mail(subject=f"PHONE VERIFICATION CODE", html_content=msg, from_email="DROPS TECHNOLOGY LIMITED <noreply@dropsride.com>", recipient_list=[user.email])

    try:
        response = api_instance.send_omnimessage(omnimessage)
        payload = {
            'head': "VERIFICATION CODE SENT",
            'body': f"please find attached your verification code: {new_code}\n\nYou can also verify by clicking the link below\n\n{domain}{link}",
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': f"{domain}{link}",
        }
        send_user_notification(user=user, payload=payload, ttl=1000)

        LOGGER.info(
            "[PHONE VERIFICATION SUCCESS] Successfully sent Omnimessage with id: %s that consists of the following messages:"
            % response.omnimessage_id
        )
        for message in response.messages:
            LOGGER.info(message)
        return JsonResponse(status=200, data={"message":"New code generated for verification", "title":"VERIFY PHONE CODE"})
    except ApiException as exception:
        LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)
        return JsonResponse(status=400, data={"message":"New code generation failed", "title":"VERIFY PHONE CODE"})

class VerifyPhone(FormView):
    """This view verifies a users phone number by checking if the code sent to
    a users phone number validates against the random 4 digit code created when
    they were creating their user account registration.

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    template_name = "account/phone_verify.html"
    form_class = ValidatePhoneForm
    success_url = reverse_lazy("account_login")

    def post(self, request, *args, **kwargs):

        code = request.POST.get('verified_code')
        if "__field_name__" in request.POST:
            return self.validate_field(request)

        instance = get_object_or_404(VerifiedPhone, code=code)
        if timezone.now() > instance.endtime:
            fmins = datetime.datetime.now() + datetime.timedelta(minutes=5)
            new_code = random_code_generator(instance)
            VerifiedPhone.objects.filter(user=instance.user, code=instance.code, verified=False).update(code=new_code, endtime=fmins)
            # instance.code = random_code_generator(instance)
            configuration = Configuration()
            configuration.username = settings.MESSENTE_API_USERNAME
            configuration.password = settings.MESSENTE_API_PASSWORD

            api_instance = OmnimessageApi(ApiClient(configuration))

            sms = SMS(sender="+2347069916149", text=f"The verification code had expired. \nPlease verify within 5 mins time to avoid code expiration again.\n\nYour new code is: {new_code}")

            omnimessage = Omnimessage(messages=tuple([sms]), to=instance.user.phone_number)

            domain = "https://www.dropsride.com" if settings.PRODUCTION else "http://localhost:8000"
            link = reverse("sms_verify", kwargs={"code":new_code, "user":instance.user})

            msg = f"""
            Dear {instance.user.username.title()},
            <br>
            <br>
            Your previous verification code expired.<br>
            please find attached your new verification code: {new_code}
            <br>
            You can also verify by clicking the link below\n\n{domain}{link}
            <br>
            """
            send_html_mail(subject=f"PHONE VERIFICATION CODE", html_content=msg, from_email="DROPS TECHNOLOGY LIMITED <noreply@dropsride.com>", recipient_list=[instance.user.email])


            try:
                response = api_instance.send_omnimessage(omnimessage)
                LOGGER.info(
                    "[PHONE VERIFICATION SMS SENT SUCCESSFULLY] Successfully sent Omnimessage with id: %s that consists of the following messages:"
                    % response.omnimessage_id
                )
                for message in response.messages:
                    LOGGER.info(message)
                return JsonResponse(status=200, data={"message":"Phone Number was resent successfully", "title":"CODE RESENT SUCCESSFULLY"})
            except ApiException as exception:
                LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)
                return JsonResponse(status=403, data={"message":exception, "title":"PHONE VERIFICATION ERROR"})
        else:
            if VerifiedPhone.objects.filter(user=instance.user, code=code, verified=False).exists():
                VerifiedPhone.objects.filter(user=instance.user, code=code, verified=False).update(verified=True, verified_code=code)
                return JsonResponse(status=201, data={"message":"Phone Number was Successfully Verified", "title":"Successful Verification"})
            else:
                return JsonResponse(status=403, data={"message":"Invalid Verification Code Used", "title":"Phone Verification Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = ValidatePhoneForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

verify_phone_number = VerifyPhone.as_view()

class UserSignupView(SignupView):
    """This is allauth default signup view which we inherit here to add our custom
    error alerts which works with axios post request. This can also be abdopted to
    create custom signup for drivers, admins and even companies willing to get
    their teams in groups to be conveyed by the platform

    Args:
        SignupView (_type_): _description_
    """

    form_class = UserSignupForm
    template_name = "account/signup.html"
    success_url = reverse_lazy('users:verify_phone')

    def get_success_url(self):
        return reverse('users:verify_phone')

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserSignupForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

account_singup = UserSignupView.as_view()

class DriverSignupView(SignupView):
    """This is allauth default signup view which we inherit here to add our custom
    error alerts which works with axios post request. This can also be abdopted to
    create custom signup for drivers, admins and even companies willing to get
    their teams in groups to be conveyed by the platform

    Args:
        SignupView (_type_): _description_
    """
    form_class = DriverSignupForm
    template_name = "account/driver_signup.html"
    success_url = reverse_lazy('users:verify_phone')

    def get_success_url(self):
        return reverse('users:verify_phone')


    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = DriverSignupForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

driver_singup = DriverSignupView.as_view()

class CompanySignupView(SignupView):
    """This is allauth default signup view which we inherit here to add our custom
    error alerts which works with axios post request. This can also be abdopted to
    create custom signup for drivers, admins and even companies willing to get
    their teams in groups to be conveyed by the platform

    Args:
        SignupView (_type_): _description_
    """
    template_name = "account/company_signup.html"
    form_class = CompanySignupForm
    success_url = reverse_lazy('users:verify_phone')

    def get_success_url(self):
        return reverse('users:verify_phone')

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = CompanySignupForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

company_singup = CompanySignupView.as_view()

class UserLoginView(LoginView):
    """Our custom user login view inheriting from allauth loginview to trigger our custom


    Args:
        LoginView (_type_): _description_
    """

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserLoginForm(request.POST)
        user = User.objects.get(email=request.POST.get('login')) if User.objects.filter(email=request.POST.get('login')).exists() else None
        avatar = user.image.url if user.image else "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
            "avatar": avatar,
        })

account_login = UserLoginView.as_view()

class EmailConfirmView(ConfirmEmailView):
    def post(self, request, *args, **kwargs):
        # if "__field_name__" in request.POST:
        #     return self.validate_field(request)

        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        # In the event someone clicks on an email confirmation link
        # for one account while logged into another account,
        # logout of the currently logged in account.
        if (
            self.request.user.is_authenticated
            and self.request.user.pk != confirmation.email_address.user_id
        ):
            self.logout()

        get_adapter(self.request).add_message(
            self.request,
            messages.SUCCESS,
            "account/messages/email_confirmed.txt",
            {"email": confirmation.email_address.email},
        )
        if app_settings.LOGIN_ON_EMAIL_CONFIRMATION:
            resp = self.login_on_confirm(confirmation)
            if resp is not None:
                return resp
        # Don't -- allauth doesn't touch is_active so that sys admin can
        # use it to block users et al
        #
        # user = confirmation.email_address.user
        # user.is_active = True
        # user.save()
        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
        # return redirect()
        return JsonResponse(status=201, data={"message":"You have successfully confirmed your email address and verified your account.", "title":"Email Confirmed", "redirect":redirect_url})

confirm_email = EmailConfirmView.as_view()

class UserPasswordChangeView(PasswordChangeView):
    # def form_valid(self, form):
    #     success_url = self.success_url
    #     form.save()
    #     logout_on_password_change(self.request, form.user)
    #     get_adapter(self.request).add_message(
    #         self.request,
    #         messages.SUCCESS,
    #         "account/messages/password_changed.txt",
    #     )
    #     signals.password_changed.send(
    #         sender=self.request.user.__class__,
    #         request=self.request,
    #         user=self.request.user,
    #     )
    #     return JsonResponse(status=200, data={"message":"your password was changed successfully", "title":"Password Change Successful"})

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

password_change = UserPasswordChangeView.as_view()

class UserPasswordSetView(PasswordSetView):
    # def form_valid(self, form):
    #     logout_on_password_change(self.request, form.user)
    #     get_adapter(self.request).add_message(
    #         self.request, messages.SUCCESS, "account/messages/password_set.txt"
    #     )
    #     signals.password_set.send(
    #         sender=self.request.user.__class__,
    #         request=self.request,
    #         user=self.request.user,
    #     )
    #     return JsonResponse(status=200, data={"message":"You have successfully set your password", "title":"Password Set Successful"})

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

password_set = UserPasswordSetView.as_view()


class UserPasswordResetFromKey(PasswordResetFromKeyView):

    # def form_valid(self, form):
    #     form.save()
    #     adapter = get_adapter(self.request)

    #     if self.reset_user and app_settings.LOGIN_ATTEMPTS_LIMIT:
    #         # User successfully reset the password, clear any
    #         # possible cache entries for all email addresses.
    #         for email in self.reset_user.emailaddress_set.all():
    #             adapter._delete_login_attempts_cached_email(
    #                 self.request, email=email.email
    #             )

    #     adapter.add_message(
    #         self.request,
    #         messages.SUCCESS,
    #         "account/messages/password_changed.txt",
    #     )
    #     signals.password_reset.send(
    #         sender=self.reset_user.__class__,
    #         request=self.request,
    #         user=self.reset_user,
    #     )

    #     if app_settings.LOGIN_ON_PASSWORD_RESET:
    #         return perform_login(
    #             self.request,
    #             self.reset_user,
    #             email_verification=app_settings.EMAIL_VERIFICATION,
    #         )
    #     return JsonResponse(status=200, data={"message":"Your password has successfully been changed", "title":"Password Reset Done"})

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

password_reset_from_key = UserPasswordResetFromKey.as_view()

class UserPasswordReset(PasswordResetView):

    # def form_valid(self, form):
    #     r429 = ratelimit.consume_or_429(
    #         self.request,
    #         action="reset_password_email",
    #         key=form.cleaned_data["email"].lower(),
    #     )
    #     if r429:
    #         return r429
    #     form.save(self.request)
    #     return JsonResponse(status=200, data={"message":"Your password has successfully been reset", "title":"Password Reset Done"})

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

password_reset = UserPasswordReset.as_view()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User's Profile"
        obj = self.request.user
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()
        return context


user_detail_view = UserDetailView.as_view()



# -----------------------------------------------------------------------------
# User update views
# -----------------------------------------------------------------------------

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    success_message = _("Information successfully updated")

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserUpdateForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        context['title'] = "Update Basic Information"
        context['description'] = "Update your basic informations"
        obj = self.request.user
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()
        return context

    def form_valid(self, form):
        try:
            form.save()
            return JsonResponse({"status":200, "title":"UPDATE DETAILS", "message":"You have successfully updated your BAsic Information."})
        except:
            return JsonResponse({"status":400, "title":"UPDATE DETAILS", "message":"Your action to update your details failed."})

user_update_view = UserUpdateView.as_view()



class UserUpdatePhoto(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserUpdateImageForm

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST or "__field_name__" in request.FILES:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserUpdateImageForm(request.POST, request.FILES)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":200, "title":"Updated Display Photo", "message":"You have successfully updated your Display Photo."})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Photo / Display Photo"
        context['description'] = "A picture is worth a thousand words."
        context['object'] = self.get_object()
        obj = self.request.user
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()

        return context


user_update_photo = UserUpdatePhoto.as_view()

class UserUpdateAddress(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserAddressForm

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST :
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserAddressForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":200, "title":"Updated Details successfully", "message":"You have successfully updated your Display Photo."})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Address"
        context['description'] = "Only for riders."
        context['object'] = self.get_object()
        obj = self.request.user
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()
        return context


user_update_address = UserUpdateAddress.as_view()


class UserUpdateSocial(LoginRequiredMixin, UpdateView):

    model = UserSocialAccounts
    form_class = UserUpdateSocialAccounts

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserUpdateSocialAccounts(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_object(self):
        return self.request.user.user_social_accounts

    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":200, "title":"Updated Social Accounts", "message":"You have successfully updated your Social Account Details."})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Social Accounts Info"
        context['description'] = "easily get follows by adding your social account details."
        context['object'] = self.get_object()
        obj = self.request.user
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()
        return context


user_update_social_accounts = UserUpdateSocial.as_view()

class AddNextOfKinView(LoginRequiredMixin, UpdateView):
    """This adds a single next of kin for the user to be contacted
    when there is an emergency

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = UserNextOfKin
    template_name = "users/user_form.html"
    form_class = AddNextOfKin


    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        return super().post(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.next_of_kin

    def form_valid(self, form):
        form.save()
        return JsonResponse(status=200, data={"message":"You have successfully added a next of kin", "title":"Next of Kin Detail"})

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddNextOfKin(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.request.user
        context['title'] = "Update Next of Kin"
        context['description'] = "This person will be contacted to ensure they are familiar with you. Submitting the form consents to us making a verification call on your behalf."
        context['object'] = obj
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver and not obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.company.get_addresses()
        return context


add_next_of_kin = AddNextOfKinView.as_view()

# ----------------------------------------------------------------------------
# End User Update Views
# ---------------------------------------------------------------------------



# ______________________________________________________________________ #
# function based views for user switches between driver and rider
# ______________________________________________________________________ #
@login_required
def driver_switch(request):
    if request.method == "POST":
        switched = request.POST.get("switched")
        if switched == "on":
            User.objects.filter(username=request.user.username).update(is_driver=True)
            # redirect(f"/users/driver/switch/?next=/{request.path}")
            return JsonResponse({"status":200, "message":"Switched to Driver"})
        else:
            User.objects.filter(username=request.user.username).update(is_driver=False)
            # redirect(f"/users/driver/switch/?next=/{request.path}")
            return JsonResponse({"status":200, "message":"Switched to Rider"})

# ______________________________________________________________________ #
# end of driver switch between driver and rider
# ______________________________________________________________________ #


# ______________________________________________________________________ #
# class based validation views for bank account and card numbers
# ______________________________________________________________________ #
class AddBankAccountDetails(LoginRequiredMixin, FormView):
    """This verifies a users account details and provides errors where form is
    invalid to axios before saving to the database

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = BankAccount
    template_name = "users/user_form.html"
    form_class = AddBankAccountForm

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            form = form.save(commit=False)
            form.user = self.request.user
            form.verified = True
            if self.request.user.first_name in self.request.POST.get['acc_name'] and self.request.user.last_name in self.request.POST.get['acc_name']:
                form.save()
                return JsonResponse(status=201, data={"message":"You have successfully added a new bank account detail", "title":"New Bank Detail"})
            return JsonResponse(status=400, data={"message":"Your name does not match with the bank accound detail", "title":"Bank Name Mismatch"})
        except:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Bank Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddBankAccountForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.request.user
        context['object'] = obj
        context['title'] = "Add Bank Account"
        context['description'] = "Save a bank account to easily transfer to. For drivers only."
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver:
            context['addresses'] = obj.company.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        return context

add_account_details = AddBankAccountDetails.as_view()


class AddCard(LoginRequiredMixin, CreateView):
    """This verifies a users debit/credit card before saving to the database

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = SavedCards
    template_name = "users/user_form.html"
    form_class = AddCardForm

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()


    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # try:
        form = form.save(commit=False)
        form.user = self.request.user
        form.active = True
        form.save()
        return JsonResponse(status=201, data={"message":"You have successfully added a new card detail", "title":"New Card Detail"})
        # except:
        #     return JsonResponse(status=400, data={"message":"Invalid card", "title":"Card Validation Error"})

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddCardForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.request.user
        context['title'] = "Add Bank Card"
        context['description'] = "Save a bank card to easily make transactions within the app"
        context['object'] = obj
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver:
            context['addresses'] = obj.company.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        return context

add_new_card = AddCard.as_view()

class UpdateCard(LoginRequiredMixin, UpdateView):
    """This verifies a users debit/credit card before saving to the database

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = SavedCards
    template_name = "users/user_form.html"
    form_class = UpdateCardForm

    def get_object(self):
        obj = get_object_or_404(SavedCards, pk=self.kwargs.get('pk'))
        return obj

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()


    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # try:
        form = form.save(commit=False)
        form.save()
        return JsonResponse(status=201, data={"message":"You have successfully updated your card detail", "title":"New Card Detail"})
        # except:
        #     return JsonResponse(status=400, data={"message":"Invalid card", "title":"Card Validation Error"})

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddCardForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.request.user
        context['title'] = "Update Bank Card"
        context['description'] = "Update your bank card or delete it if necessary"
        context['object'] = obj
        context['email'] = EmailAddress.objects.get(user=obj, email=obj.email) if EmailAddress.objects.filter(user=obj, email=obj.email) else None
        if not obj.is_driver:
            context['addresses'] = obj.company.get_addresses()
        elif obj.is_company:
            context['addresses'] = obj.rider.get_addresses()
        return context

update_card = UpdateCard.as_view()


# ______________________________________________________________________ #
# end class based validation views for bank account and card numbers
# ______________________________________________________________________ #
def remove_card(request, pk):
    if not request.user.is_authenticated:
        return reverse_lazy('account_login')

    card = get_object_or_404(SavedCards, pk=pk)

    if request.method == 'POST':
        card.delete()
        return JsonResponse(status=200, data={'title':"Card Deleted", 'message':'You have successfully deleted this card'})

    addresses = request.user.rider.get_addresses() if not request.user.is_driver else request.user.company.get_addresses()
    context = {
        'object': request.user,
        'title':"Remove Bank Card",
        'description':"Are you sure you want to remove this bank card?",
        'card':card,
        'email':EmailAddress.objects.get(user=request.user, email=request.user.email) if EmailAddress.objects.filter(user=request.user, email=request.user.email) else None,
        'card': True,
        'addresses' : addresses

    }

    return render(request, "users/form.html", context)

def remove_bank(request, pk):
    if not request.user.is_authenticated:
        return reverse_lazy('account_login')

    card = get_object_or_404(BankAccount, pk=pk)

    if request.method == 'POST':
        card.delete()
        return JsonResponse(status=200, data={'title':"Bank Account Deleted", 'message':f'You have successfully deleted this bank account {card.acc_no}'})

    addresses = request.user.rider.get_addresses() if not request.user.is_driver else request.user.company.get_addresses()
    context = {
        'object': request.user,
        'title':"Remove Bank Account",
        'description':f"Are you sure you want to remove this bank Account: {card.acc_no}?",
        'card':card,
        'email':EmailAddress.objects.get(user=request.user, email=request.user.email) if EmailAddress.objects.filter(user=request.user, email=request.user.email) else None,
        'card':False,
        'addresses' : addresses

    }

    return render(request, "users/form.html", context)

