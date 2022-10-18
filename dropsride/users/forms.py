from datetime import datetime
import requests
import pprint

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils import timezone

from allauth.account.forms import SignupForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from countries_plus.models import Country
from dropsride.companies.models import Company

from paystackapi.verification import Verification


from dropsride.currency.models import Banks
from dropsride.utils.logger import LOGGER
from dropsride.users.models import BankAccount, SavedCards, UserNextOfKin, UserSocialAccounts, VerifiedPhone

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = ("first_name", "middle_name", "last_name", "username", "email", "gender", "date_of_birth", "country", "gave_consent")

class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("first_name", "middle_name", "last_name", "username", "email", "gender", "date_of_birth", "country", "gave_consent", 'password1', 'password2')

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "middle_name", "last_name", "country", "date_of_birth"]

class UserUpdateImageForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["image"]

class AddNextOfKin(forms.ModelForm):
    class Meta:
        model = UserNextOfKin
        fields = [
            'name',
            'address',
            'city',
            'state',
            'country',
            'latitude',
            'longitude',
            'image'
        ]

class AddBankAccountForm(forms.ModelForm):
    class Meta:
      model = BankAccount
      fields = [
            'bank',
            'acc_no',
            'acc_name',
            'bvn',
      ]

    def clean_bvn(self):
        acc_no = self.cleaned_data["acc_no"]
        data = self.cleaned_data["bvn"]
        bank = self.cleaned_data['bank']
        b_code = get_object_or_404(Banks, name=bank.name).code
        response = Verification.verify_bvn_match(account_number=acc_no, bvn=data, bank_code=b_code)
        if response.data.verified == False:
            return ValidationError("This account number is not valid")
        return data


class AddCardForm(forms.ModelForm):
    class Meta:
        model = SavedCards
        fields = [
            'name_on_card',
            'card_no',
            'card_exp_month',
            'card_exp_year',
        ]
    def clean_card_no(self):
        data = self.cleaned_data["card_no"]
        url = f"https://api.paystack.co/decision/bin/{data[:6]}"
        if not settings.PRODUCTION:
            headers = {
                'Authorization': str(settings.PAYSTACK_TEST_SK),
            }
        else:
            headers = {
                'Authorization': str(settings.PAYSTACK_LIVE_SK),
            }

        response = requests.request("GET", url, headers=headers)
        response = response.json()
        LOGGER.info(response)
        if response['status'] == False:
            return ValidationError("This card number is not valid")
        return data

    def clean_card_exp_year(self):
        data = self.cleaned_data['card_exp_year']
        month = self.cleaned_data['card_exp_month']
        if int(timezone.now().year) > int(data):
            return ValidationError("This card has already expired and cannot be used")
        elif int(timezone.now()) < int(month) and int(timezone.now().year) == int(data):
            return ValidationError("This card will be expiring soon")
        return data


class UserUpdateSocialAccounts(forms.ModelForm):
    class Meta:
        model = UserSocialAccounts
        fields = [
            "facebook",
            "twitter",
            "instagram",
        ]

    def clean_facebook(self):
        data = self.cleaned_data('facebook')
        if UserSocialAccounts.objects.filter(facebook=data):
            raise ValidationError(mark_safe("This profile has already been used. If you are sure this is not you, please contact <a class='text-blue-600 font-bold' href='mailto://dispute@dropsride.com'>mailto://dispute@dropsride.com</a>"))
        return data

    def clean_twitter(self):
        data = self.cleaned_data('twitter')
        if UserSocialAccounts.objects.filter(twitter=data):
            raise ValidationError(mark_safe("This profile has already been used. If you are sure this is not you, please contact <a class='text-blue-600 font-bold' href='mailto://dispute@dropsride.com'>mailto://dispute@dropsride.com</a>"))
        return data

    def clean_instagram(self):
        data = self.cleaned_data('instagram')
        if UserSocialAccounts.objects.filter(instagram=data):
            raise ValidationError(mark_safe("This profile has already been used. If you are sure this is not you, please contact <a class='text-blue-600 font-bold' href='mailto://dispute@dropsride.com'>mailto://dispute@dropsride.com</a>"))
        return data

class ValidatePhoneForm(forms.ModelForm):

    class Meta:
        model = VerifiedPhone
        fields = ['verified_code']

    def clean_verified_code(self):
        verified_code = self.cleaned_data['verified_code']

        if VerifiedPhone.objects.filter(code=verified_code, verified=True).exists():
            raise ValidationError("This code has already been used")
        return verified_code

class UserAddressForm(forms.ModelForm):
    address = forms.CharField(max_length=250, required=True, widget=forms.HiddenInput())
    city = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    state = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = [
            'address',
            'city',
            'post_code',
            'state',
            'country',
            'latitude',
            'longitude',
        ]




class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    # first_name = forms.CharField(max_length=30, label='First Name')
    # middle_name = forms.CharField(max_length=30, label='Middle Name')
    # last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=13, min_length=11, label='Phone Number')
    token = forms.CharField(widget=forms.HiddenInput())
    # gender = forms.ChoiceField(choices=User.GENDER)
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="(Country)")
    # date_of_birth = forms.DateField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 4:
            raise ValidationError('Username is too short')

        if ("admin", "superuser", "administrator") in username:
            raise ValidationError("Unavailable username parameters")

        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if ("admin", "superuser", "administrator") in email:
            raise ValidationError("Unavailable email name parameters")

        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if "+" in phone_number:
            raise ValidationError("Phone number should start with your country code eg: +234, +1")

        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("A user with this phone number already exists")
        return phone_number

    def save(self, request):
        user = super().save(request)
        user.gave_consent = True
        user.save()
        return user

class CompanySignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    # first_name = forms.CharField(max_length=30, label='First Name')
    # middle_name = forms.CharField(max_length=30, label='Middle Name')
    # last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=13, min_length=11, label='Phone Number')
    company_name = forms.CharField(max_length=500, min_length=11, label='Company Name')
    token = forms.CharField(widget=forms.HiddenInput())
    # gender = forms.ChoiceField(choices=User.GENDER)
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="(Country)")
    # date_of_birth = forms.DateField()

    def clean_company_name(self):
        data = self.cleaned_data('company_name')
        cp = get_object_or_404(Company, company_name=data)
        if Company.objects.filter(company_name=data).exists():
            raise ValidationError(f"This company has already been registered by {cp.user.get_full_name()}. Please contact this email: {cp.user.email} to seek permission to this account or be added as an admin")
        return data


    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 4:
            raise ValidationError('Username is too short')

        if ("admin", "superuser", "administrator") in username:
            raise ValidationError("Unavailable username parameters")

        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if ("admin", "superuser", "administrator") in email:
            raise ValidationError("Unavailable email name parameters")

        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if "+" in phone_number:
            raise ValidationError("Phone number should start with your country code eg: +234, +1")

        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("A user with this phone number already exists")
        return phone_number

    def save(self, request):
        user = super().save(request)
        user.gave_consent = True
        user.is_company = True
        user.save()
        return user



class UserLoginForm(LoginForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise ValidationError("You are not registered with us. Please signup as a driver, or a fleet owner")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("You are not registered with us. Please signup as a driver, or a fleet owner")
        return email


class DriverSwitchForm(forms.ModelForm):
    """Swith between driver and rider

    Args:
        forms (_type_): _description_
    """
    pass

    class Meta:
        model = User
        fields = ["is_driver"]



class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
