from datetime import date
import datetime
from enum import unique

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    URLField,
    DateTimeField,
    FloatField,
    TextField,
    TimeField,
    IntegerField,
    PositiveSmallIntegerField,
    PositiveBigIntegerField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    GenericIPAddressField,
    Sum
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from dropsride.currency.models import Banks
from django.core.exceptions import ValidationError

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country
from tinymce.models import HTMLField


class User(AbstractUser):
    """
    Default custom user model for dropsride.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    MALE = "M"
    FEMALE = "F"
    NONE = "NA"
    GENDER = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (NONE, "NONE")
    )


    #: First and last name do not cover name patterns around the globe
    company_name = CharField(_("Middle Name"), blank=True, max_length=255)
    middle_name = CharField(_("Middle Name"), blank=True, max_length=255)
    last_ip = GenericIPAddressField(blank=True, null=True)
    phone_number = CharField(max_length=15, blank=True, null=True)
    ref_link = CharField(_("Referral Link"), max_length=500, blank=True)
    gender = CharField(_("Gender"), blank=True, max_length=3, choices=GENDER, default=NONE)
    date_of_birth = DateField(_("Date of birth"), blank=True, null=True)

    address = CharField(max_length=500, blank=True, null=True)
    city = CharField(max_length=500, blank=True, null=True)
    post_code = CharField(max_length=500, blank=True, null=True)
    state = CharField(max_length=500, blank=True, null=True)
    # country = CharField(max_length=500)
    latitude = CharField(max_length=500, blank=True, null=True)
    longitude = CharField(max_length=500, blank=True, null=True)
    country = ForeignKey(Country, on_delete=DO_NOTHING, verbose_name=_("Country"), blank=True, null=True)

    image = StdImageField(_("Display Photo"), upload_to="user/passport", blank=True, delete_orphans=True, variations={'thumbnail': {"width": 100, "height": 100, "crop": True}})

    is_driver = BooleanField(default=False)
    is_company = BooleanField(default=False)

    captcha_score = FloatField(default=0.00)
    gave_consent = BooleanField(_("Share my registration data with readville's content providers for marketing purposes. This confirms you are up to the legal age approved in your country."), default=False)

    def __str__(self):
        return self.username

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_user_banks(self):
        if self.bank_account:
            return self.bank_account.filter(verified=True)
        return None

    def get_user_cards(self):
        if self.saved_card:
            return self.saved_card.all()
        return None

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class VerifiedPhone(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="verified_phone")
    code = CharField(max_length=4, blank=True, null=True, unique=True)
    verified_code = CharField(max_length=4, blank=True, null=True)
    time = TimeField(blank=True, null=True)
    endtime = DateTimeField(blank=True, null=True)

    verified = BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        verbose_name = "Verified Phone Number"
        verbose_name_plural = "Verified Phone Numbers"
        ordering = ["-created"]


class UserSocialAccounts(TimeStampedModel):
    """This holds all social accounts for a certain user

    Args:
        TimeStampedModel (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = OneToOneField(User, on_delete=CASCADE, related_name="user_social_accounts")
    facebook = URLField(_("Facebook"), blank=True)
    twitter = URLField(_("Twitter"), blank=True)
    instagram = URLField(_("Instagram"), blank=True)

    def __str__(self):
        return f"{self.user.username} social accounts"

    class Meta:
        managed = True
        verbose_name = "User Social Accounts"
        verbose_name_plural = "Users Social Accounts"
        ordering = ["-user__date_joined"]


class UserNextOfKin(TimeStampedModel):
    """Add a next of kin detail in case of emergency

    Args:
        TimeStampedModel (_type_): _description_
    """

    user = OneToOneField(User, related_name='next_of_kin', on_delete=CASCADE)
    name = CharField(max_length=500, help_text="ensure the name 'corresponds/is exactly' the same with their registered BVN")
    phone_number = CharField(max_length=15, blank=True, null=True)
    address = CharField(max_length=500)
    city = CharField(max_length=500)
    state = CharField(max_length=500)
    country = CharField(max_length=500)
    latitude = CharField(max_length=500)
    longitude = CharField(max_length=500)

    verified = BooleanField(default=False)

    image = StdImageField(_("Passport"), upload_to="user/nok/passport", blank=True, delete_orphans=True, variations={'thumbnail': {"width": 100, "height": 100, "crop": True}})

    def __str__(self):
        return f"{self.user.username.upper()} Next of Kin: {self.name.title()}"

    class Meta:
        managed = True
        verbose_name = "User Next of Kin"
        verbose_name_plural = "Users Next of Kin"
        ordering = ["-created"]


class SavedCards(TimeStampedModel):
    """Save transactional ATM Cards for use when ever making purchases

    Args:
        TimeStampedModel (_type_): _description_
    """

    user = ForeignKey(User, on_delete=CASCADE, related_name="saved_card")
    name_on_card = CharField(max_length=255)
    card_no = CharField(max_length=18, unique=True)
    cvv = CharField(max_length=18, blank=True, null=True)
    card_exp_month = CharField(max_length=2, blank=True)
    card_exp_year = CharField(max_length=4, blank=True)
    card_provider = CharField(max_length=40, default="master")

    active = BooleanField(default=False)

    @property
    def formatted_no(self):
        formatted = f"{self.card_no[:4]}-{self.card_no[4:8]}-{self.card_no[8:12]}-{self.card_no[12:]}"
        return formatted

    @property
    def expired(self):
        if datetime.datetime.now().month > int(self.card_exp_month) and datetime.datetime.now().year >= int(self.card_exp_year):
            return True
        return False


    def __str__(self):
        return f"{self.user.username.upper()} Saved Card: {self.card_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Card"
        verbose_name_plural = "User Saved Cards"
        ordering = ["-created", 'active']



class BankAccount(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="bank_account")
    bank = ForeignKey(Banks, on_delete=DO_NOTHING, related_name="bank_account")
    acc_no = CharField(max_length=17, unique=True)
    acc_name = CharField(max_length=255)
    bvn = CharField(max_length=11)

    verified = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username.upper()} Saved Bank Account: {self.acc_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Bank"
        verbose_name_plural = "User Saved Banks"
        ordering = ["-modified", "verified"]




















