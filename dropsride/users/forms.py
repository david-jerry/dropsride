from allauth.account.forms import LoginForm, SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.conf import settings
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.gis import forms
from django.utils.translation import gettext_lazy as _

from dropsride.currency.models import Currency
from dropsride.utils.logger import LOGGER

from .models import (
    BankAccount,
    NextOfKin,
    Profile,
    SavedCards,
    VerifiedDocuments,
    Wallet,
)

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserLoginForm(LoginForm):
    """
    login form defaults
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3)


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    first_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    gender = forms.ChoiceField(choices=User.GENDER, widget=forms.Select())

    is_driver = forms.BooleanField(widget=forms.CheckboxInput())
    gave_consent = forms.BooleanField(widget=forms.CheckboxInput())

    captcha = ReCaptchaField(widget=ReCaptchaV3)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "phone",
            "date_of_birth",
            "bvn",
            "address",
            "town",
            "county",
            "post_code",
            "country",
        ]
        widgets = {
            "address": forms.HiddenInput(),
            "town": forms.HiddenInput(),
            "county": forms.HiddenInput(),
            "post_code": forms.HiddenInput(),
            "country": forms.HiddenInput(),
        }


class UpdateProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class AddNextOfKin(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "email",
            "bvn",
            "phone",
            "address",
            "town",
            "county",
            "post_code",
            "country",
            "longitude",
            "latitude",
        ]
        widgets = {
            "address": forms.HiddenInput(),
            "town": forms.HiddenInput(),
            "county": forms.HiddenInput(),
            "post_code": forms.HiddenInput(),
            "country": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
            "latitude": forms.HiddenInput(),
        }


class AddDocumentsForm(forms.ModelForm):
    class Meta:
        model = VerifiedDocuments
        fields = [
            "license",
            "license_exp",
            "proof_of_ownership",
            "vehicle_license",
            "autocheck_certificate",
            "insurance",
        ]
        widget = {"license_exp": forms.HiddenInput()}


class AddCardForm(forms.ModelForm):
    class Meta:
        model = SavedCards
        fields = [
            "name_on_card",
            "card_no",
            "card_exp_month",
            "card_exp_year",
            "card_provider",
        ]


class UpdateCardForm(forms.ModelForm):
    class Meta:
        model = SavedCards
        fields = [
            "name_on_card",
            "card_no",
            "card_exp_month",
            "card_exp_year",
            "card_provider",
            "active",
        ]


class UserWalletForm(forms.ModelForm):
    currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(), empty_label="(Currency)"
    )

    class Meta:
        model = Wallet
        fields = ["currency"]


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
