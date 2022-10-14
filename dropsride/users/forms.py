from allauth.account.forms import SignupForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from countries_plus.models import Country

from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dropsride.users.models import UserSocialAccounts

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

class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    first_name = forms.CharField(max_length=30, label='First Name')
    middle_name = forms.CharField(max_length=30, label='Middle Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=13, min_length=11, label='Phone Number')
    gender = forms.ChoiceField(choices=User.GENDER)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="(Country)")
    date_of_birth = forms.DateField()

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
        user.consent = True
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


class SociaProfileLinks(forms.ModelForm):
    class Meta:
        model = UserSocialAccounts
        exclude = ["created", "modified", "user"]


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
