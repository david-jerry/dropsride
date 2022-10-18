import asyncio
from dropsride.companies.models import Company
from dropsride.utils.logger import LOGGER
import httpx
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, ListView, FormView
from django.http import JsonResponse
from django.utils import timezone

from allauth import app_settings
from allauth.account.views import SignupView, LoginView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse
from paystackapi.paystack import Paystack
from paystackapi.verification import Verification
from asgiref.sync import sync_to_async
from messente_api import OmnimessageApi, SMS, Omnimessage, Configuration, ApiClient
from messente_api.rest import ApiException

from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.users.models import UserNextOfKin, UserSocialAccounts, VerifiedPhone
from dropsride.users.forms import AddBankAccountForm, AddCardForm, AddNextOfKin, CompanySignupForm, UserAddressForm, UserLoginForm, UserSignupForm, UserUpdateForm, UserUpdateImageForm, UserUpdateSocialAccounts, ValidatePhoneForm
from dropsride.utils.unique_generators import random_code_generator

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
    five_min = instance.modified.minutes + timedelta(minutes=5)
    if timezone.now() > five_min:
        instance.code = random_code_generator(instance)
        configuration = Configuration()
        configuration.username = settings.MESSENTE_API_USERNAME
        configuration.password = settings.MESSENTE_API_PASSWORD

        api_instance = OmnimessageApi(ApiClient(configuration))

        sms = SMS(sender="Drops Technology Limited", text=f"The verification code had expired. \nPlease verify within 5 mins time to avoid code expiration again.\n\nYour new code is: {instance.code}")

        omnimessage = Omnimessage(messages=tuple([sms]), to=instance.user.phone_number)

        try:
            response = api_instance.send_omnimessage(omnimessage)
            LOGGER.info(
                "[PHONE VERIFICATION SUCCESS] Successfully sent Omnimessage with id: %s that consists of the following messages:"
                % response.omnimessage_id
            )
            for message in response.messages:
                LOGGER.info(message)
            return JsonResponse(status=200, data={"message":"Reverification sms has been sent to your registered mobile line", "title":"Verification Code Expired"})
        except ApiException as exception:
            LOGGER.error("[PHONE VERIFICATION ERROR] Exception when sending an omnimessage: %s\n" % exception)
            return JsonResponse(status=400, data={"message":f"Exception when sending verification sms: %s\n{exception}", "title":"Verification Code Expired Error"})
    pass

def sms_verification_link(request, code):
    """sends the verification code via a link through the sms

    Args:
        request (_type_): http request
        code (_type_): code from the sms link

    Returns:
        _type_: _description_
    """
    instance = get_object_or_404(VerifiedPhone, code=code)
    time_out_phone_verification(instance=instance)
    if VerifiedPhone.objects.filter(code=code, verified=False).exists():
        VerifiedPhone.objects.filter(code=code, verified=False).update(verified=True, verified_code=code)
        return JsonResponse(status=201, data={"message":"Phone Number was Successfully Verified", "title":"Successful Verification"})
    else:
        return JsonResponse(status=400, data={"message":"Invalid Verification Code Used", "title":"Phone Verification Error"})

class VerifyPhone(LoginRequiredMixin, FormView):
    """This view verifies a users phone number by checking if the code sent to
    a users phone number validates against the random 4 digit code created when
    they were creating their user account registration.

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    template_name = "account/phone_verify.html"
    form_class = ValidatePhoneForm()

    def post(self, request, *args, **kwargs):

        code = request.POST.get('verified_code')
        if "__field_name__" in request.POST:
            return self.validate_field(request)

        instance = get_object_or_404(VerifiedPhone, code=code)
        time_out_phone_verification(instance)

        if VerifiedPhone.objects.filter(user=request.user, code=code, verified=False).exists():
            VerifiedPhone.objects.filter(user=request.user, code=code, verified=False).update(verified=True, verified_code=code)
            return JsonResponse(status=201, data={"message":"Phone Number was Successfully Verified", "title":"Successful Verification"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid Verification Code Used", "title":"Phone Verification Error"})


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

    def form_valid(self, form):
        form = form.save(commit=False)
        form.gave_consent = True
        form.is_driver = False
        form.is_company = False
        self.user = form.save(self.request)
        try:
            complete_signup(self.request, self.user, app_settings.EMAIL_VERIFICATION, self.get_success_url())
            return JsonResponse(status=201, data={"message":"Your Account Was Created Successfully", "title":"Successful Registration"})
        except ImmediateHttpResponse as e:
            return JsonResponse(status=400, data={"message":f"{e.response}", "title":"Signup Form Error"})

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
    form_class = UserSignupForm
    template_name = "account/driver_signup.html"

    def form_valid(self, form):
        form = form.save(commit=False)
        form.gave_consent = True
        form.is_driver = True
        form.is_company = False
        self.user = form.save(self.request)
        try:
            complete_signup(self.request, self.user, app_settings.EMAIL_VERIFICATION, self.get_success_url())
            return JsonResponse(status=201, data={"message":"Your Account Was Created Successfully", "title":"Successful Registration"})
        except ImmediateHttpResponse as e:
            return JsonResponse(status=400, data={"message":f"{e.response}", "title":"Signup Form Error"})

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

    def form_valid(self, form):
        company_name = self.request.POST.get('company_name')
        form = form.save(commit=False)
        form.gave_consent = True
        form.is_driver = False
        form.is_company = True
        self.user = form.save(self.request)
        try:
            complete_signup(self.request, self.user, app_settings.EMAIL_VERIFICATION, self.get_success_url())
            if Company.objects.filter(user=self.user).exists():
                Company.objects.filter(user=self.user).update(company_name=company_name)
                LOGGER.info("[COMPANY SIGNUP VIEW] Company name has been added")
            return JsonResponse(status=201, data={"message":"Your Account Was Created Successfully", "title":"Successful Registration"})
        except ImmediateHttpResponse as e:
            return JsonResponse(status=400, data={"message":f"{e.response}", "title":"Signup Form Error"})

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
    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            form.login(self.request, redirect_url=success_url)
            return JsonResponse(status=201, data={"message":"Logged In Successfully", "title":"Success"})
        except ImmediateHttpResponse as e:
            return JsonResponse(status=400, data={"message":f"{e.response}", "title":"Login Form Error"})

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserLoginForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

account_login = UserLoginView.as_view()



class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User's Profile"
        return context


user_detail_view = UserDetailView.as_view()



# -----------------------------------------------------------------------------
# User update views
# -----------------------------------------------------------------------------

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    form_class = UserUpdateForm()
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

    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":200, "title":"Updated Details successfully", "message":"You have successfully updated your BAsic Information."})


user_update_view = UserUpdateView.as_view()



class UserUpdatePhoto(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserUpdateImageForm()

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
        return JsonResponse({"status":200, "title":"Updated Details successfully", "message":"You have successfully updated your Display Photo."})


user_update_photo = UserUpdatePhoto.as_view()

class UserUpdateAddress(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserAddressForm()

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


user_update_address = UserUpdateAddress.as_view()


class UserUpdateSocial(LoginRequiredMixin, UpdateView):

    model = UserSocialAccounts
    form_class = UserUpdateSocialAccounts()

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


user_update_social_accounts = UserUpdateSocial.as_view()

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
class AddNextOfKinView(LoginRequiredMixin, FormView):
    """This adds a single next of kin for the user to be contacted
    when there is an emergency

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    template_name = "users/kin_form.html"
    form_class = AddNextOfKin()

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = AddNextOfKin(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if not request.user.next_of_kin:
                form.user = request.user
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully added a next of kin", "title":"Next of Kin Detail"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form", "title":"Form Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddNextOfKin(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

add_next_of_kin = AddNextOfKinView.as_view()

class AddBankAccountDetails(LoginRequiredMixin, FormView):
    """This verifies a users account details and provides errors where form is
    invalid to axios before saving to the database

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    template_name = "users/bank_form.html"
    form_class = AddBankAccountForm()

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = AddBankAccountForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully added a new bank account detail", "title":"New Bank Detail"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Bank Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddBankAccountForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

add_account_details = AddBankAccountDetails.as_view()


class AddCard(LoginRequiredMixin, FormView):
    """This verifies a users debit/credit card before saving to the database

    Args:
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    template_name = "users/card_form.html"
    form_class = AddCardForm()

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = AddCardForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully added a new card detail", "title":"New Card Detail"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid card", "title":"Card Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = AddCardForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

add_new_card = AddCard.as_view()

# ______________________________________________________________________ #
# end class based validation views for bank account and card numbers
# ______________________________________________________________________ #
