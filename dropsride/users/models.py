from datetime import date

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
    TextField,
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
    middle_name = CharField(_("Middle Name"), blank=True, max_length=255)
    last_ip = GenericIPAddressField(blank=True, null=True)
    phone_number = CharField(max_length=15, blank=True, null=True)
    ref_link = CharField(_("Referral Link"), max_length=500, blank=True)
    gender = CharField(_("Gender"), blank=True, max_length=3, choices=GENDER, default=NONE)
    date_of_birth = DateField(_("Date of birth"), blank=True, null=True)
    city = CharField(max_length=255, blank=True, null=True)
    country = ForeignKey(Country, on_delete=DO_NOTHING, verbose_name=_("Country"), blank=True, null=True)
    image = StdImageField(_("Display Photo"), upload_to="user/passport", blank=True, delete_orphans=True, variations={'thumbnail': {"width": 100, "height": 100, "crop": True}})

    is_driver = BooleanField(default=False)

    gave_consent = BooleanField(_("Share my registration data with readville's content providers for marketing purposes. This confirms you are up to the legal age approved in your country."), default=False)

    def __str__(self):
        return self.username

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


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

    user = ForeignKey(User, related_name='next_of_kin', on_delete=CASCADE)
    name = CharField(max_length=500, help_text="ensure the name 'corresponds/is exactly' the same with their registered BVN")
    address = CharField(max_length=500)
    city = CharField(max_length=500)
    state = CharField(max_length=500)
    country = CharField(max_length=500)
    latitude = CharField(max_length=500)
    longitude = CharField(max_length=500)

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
    card_no = CharField(max_length=18)
    card_exp_month = PositiveSmallIntegerField()
    card_exp_year = PositiveSmallIntegerField()

    expired = BooleanField(default=False)

    @property
    def exp(self):
        if timezone.now().month > self.card_exp_month and timezone.now().year >= self.card_exp_year:
            self.expired = True
            self.save()
            return True
        return False


    def __str__(self):
        return f"{self.user.username.upper()} Saved Card: {self.card_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Card"
        verbose_name_plural = "User Saved Cards"
        ordering = ["-card_no"]


class BankAccount(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="bank_account")
    bank = ForeignKey(Banks, on_delete=DO_NOTHING, related_name="bank_account")
    acc_no = CharField(max_length=17)
    acc_name = CharField(max_length=255)
    bvn = CharField(max_length=11)

    verified = BooleanField(default=False)

    def clean(self):
        if not len(self.account) > 17:
            raise ValidationError({'title': "Not a valid account number"})

    def __str__(self):
        return f"{self.user.username.upper()} Saved Bank Account: {self.acc_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Bank"
        verbose_name_plural = "User Saved Banks"
        ordering = ["-acc_name", "verified"]
