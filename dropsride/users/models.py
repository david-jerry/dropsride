from datetime import date
from decimal import Decimal

from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    EmailField,
    F,
    FileField,
    FloatField,
    ForeignKey,
    Index,
    OneToOneField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from stdimage import StdImageField

from dropsride.currency.models import Banks, Currency
from dropsride.settings.models import CarType
from dropsride.utils.validators import validate_uploaded_pdf_extension


class User(AbstractUser):
    """
    Default custom user model for dropsride.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    MALE = "M"
    FEMALE = "F"
    NONE = "LGBQ"
    GENDER = ((MALE, "MALE"), (FEMALE, "FEMALE"), (NONE, "LGBQ"))

    #: First and last name do not cover name patterns around the globe
    middle_name = CharField(_("Middle Name"), blank=True, max_length=255)
    unique_id = CharField(
        _("Registration number"), max_length=255, null=True, blank=True, db_index=True
    )
    ref_number = CharField(
        _("Referral Code"), max_length=500, blank=True, null=True, db_index=True
    )
    gender = CharField(
        _("Gender"), blank=True, max_length=10, choices=GENDER, default=NONE
    )

    recommended_by = ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=CASCADE,
        related_name="recommender",
        db_index=True,
    )

    is_driver = BooleanField(_("Driver?"), default=False, db_index=True)
    is_verified = BooleanField(_("Verified?"), default=False, db_index=True)
    gave_consent = BooleanField(
        _("Privacy Consent"),
        help_text=_(
            "Share my registration data with dropsride's content providers for marketing purposes. This confirms you are up to the legal age approved in your country."
        ),
        default=True,
    )

    customer_code = CharField(max_length=500, blank=True, null=True)

    # Google Map
    longitude = FloatField(_("User Longitude"), default=0.00)
    latitude = FloatField(_("User Latitude"), default=0.00)

    on_a_ride = BooleanField(default=False)

    @property
    def email_verified(self):
        try:
            emailaddress = EmailAddress.objects.get_for_user(self, self.email)
            result = emailaddress.verified
        except:
            result = False
        return result

    @property
    def token(self):
        return self.auth_token.key

    @property
    def name_initials(self):
        return (
            f"{self.first_name.title()[0]}{self.last_name.title()[0]}"
            if self.first_name and self.last_name
            else None
        )

    @property
    def short_name(self):
        return (
            f"{self.first_name.title()} {self.last_name.title()}"
            if self.first_name and self.last_name
            else None
        )

    @property
    def long_name(self):
        return (
            f"{self.first_name.title()} {self.middle_name.title()} {self.last_name.title()}"
            if self.first_name and self.middle_name and self.last_name
            else None
        )

    def check_verification(self):
        if (
            self.profile.profile_verified
            and self.nok.kin_verified
            and self.documents.document_verified
            and self.vehicle.vehicle_verified
        ):
            self.is_verified = True
            return self.save(update_fields=["is_verified"])
        pass

    # referral information
    @property
    def referral_bonus(self):
        currency = self.wallet.currency.symbol
        amount = self.ref_bonus.amount
        if currency != "$":
            amount *= self.wallet.currency.price
        return f"{currency} {round(amount, 2)}"

    @property
    def ref_link(self):
        """
        Returns a user's referral link
        """
        site = "localhost:8000/" if not settings.PRODUCTION else "dropsride.com/"
        protocol = "https" if settings.PRODUCTION else "http"
        return f"{protocol}://{site}ref/{self.ref_number}" if self.ref_number else ""

    @property
    def referrals(self):
        """
        Returns a list of referred users by their shortname
        """
        qs = self.__class__.objects.filter(recommended_by=self.id)
        refs = []
        for ref in qs:
            refs.append(ref.short_name)
        return refs

    @property
    def no_referrals(self):
        return len(self.referrals())

    # ride relationships

    # transaction relationships

    # ticket relationships

    # get foreignkey relationships as methods
    @property
    def get_all_banks(self):
        """
        Returns all saved bank accounts for the user, or an empty list if no banks are saved.
        """
        return self.bank_account.filter(bank_verified=True) or []

    @property
    def get_all_cards(self):
        """
        Returns all saved cards for the user, or an empty list if no cards are saved.
        """
        return self.saved_card.filter(card_verified=True) or []

    def __str__(self):
        return (
            f"{self.username.title()}"
            if not self.short_name
            else f"{self.short_name.title()}"
        )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        managed = True
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
        ordering = ["-date_joined"]
        # indexes = [
        #     Index(fields=['username']),
        #     Index(fields=['email']),
        #     Index(fields=['unique_id']),
        # ]


class ReferralBonus(TimeStampedModel):
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name="ref_bonus",
        null=True,
        blank=True,
        db_index=True,
    )
    amount = DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def get_queryset(self):
        return self.__class__.objects.filter(user=self.user)

    @transaction.atomic()
    def add_bonus(self):
        self.amount = F("amount") + Decimal(1.05)
        self.save(update_fields=["amount"])

    @transaction.atomic()
    def withdraw_bonus(self, amount):
        """This function shall accept an amount of the users choosing to withdraw from
        their bonus amount.

        Args:
            amount (decimal): user's input to be withdrawn
        """
        obj = self.get_queryset().select_for_update().get()
        if amount > obj.amount:
            raise ValidationError(
                _(f"There is insufficient bonus amount to withdraw {amount}")
            )
        obj.amount -= Decimal(amount)
        obj.save()

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER REFERRAL BONUS]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER REFERRAL BONUS]"
        )

    class Meta:
        managed = True
        verbose_name = "User Referral Bonus"
        verbose_name_plural = "User Referral Bonuses"
        ordering = ["-created"]


class Settings(TimeStampedModel):
    user = OneToOneField(
        User, on_delete=CASCADE, related_name="settings", db_index=True
    )
    email_notification = BooleanField(default=True)
    push_notification = BooleanField(default=True)
    sms_notification = BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER SETTING]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER SETTING]"
        )

    class Meta:
        managed = True
        verbose_name = "User Setting"
        verbose_name_plural = "User Settings"
        ordering = ["-modified"]


class Profile(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="profile", db_index=True)

    # personal information
    image = StdImageField(
        _("Display Photo"),
        upload_to="user/passport",
        blank=True,
        null=True,
        delete_orphans=True,
        variations={"thumbnail": {"width": 100, "height": 100, "crop": True}},
    )
    phone = CharField(_("Customer Contact"), max_length=16, blank=True)
    date_of_birth = DateField(_("Date of birth"), blank=True, null=True)
    bvn = CharField(_("Bank Verification Number"), blank=True, max_length=12)

    # address
    address = CharField(_("Customer Address"), max_length=500, blank=True, null=True)
    town = CharField(_("Customer Town/City"), max_length=120, blank=True, null=True)
    county = CharField(_("Customer County"), max_length=120, blank=True, null=True)
    state = CharField(_("Customer State"), max_length=120, blank=True, null=True)
    post_code = CharField(
        _("Customer Post Code"), max_length=120, blank=True, null=True
    )
    country = CharField(_("Customer Country"), max_length=120, blank=True, null=True)

    profile_verified = BooleanField(default=False)

    @property
    def is_profile_complete(self):
        try:
            profile = Profile.objects.get(user=self.user)
            if (
                profile.image
                and profile.phone
                and profile.date_of_birth
                and profile.address
                and profile.town
                and profile.county
                and profile.state
                and profile.post_code
                and profile.country
            ):
                self.profile_verified = True
                return self.save(update_fields=["profile_verified"]), True
        except Profile.DoesNotExist:
            pass
        return False

    @property
    def home_address(self):
        return f"{self.address}, {self.town}, {self.county}, {self.post_code}, {self.country}"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
            return age if age and age > 0 else 0
        return "NA"

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER PROFILE]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER PROFILE]"
        )

    class Meta:
        managed = True
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ["-created"]


class NextOfKin(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="nok", db_index=True)

    first_name = CharField(_("First Name"), blank=True, max_length=255)
    middle_name = CharField(_("Middle Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)
    date_of_birth = DateField(_("Date of birth"), blank=True, null=True)

    # personal information
    email = EmailField(_("Email Address"), blank=True, null=True)
    phone = CharField(_("Customer Contact"), max_length=16, blank=True)

    # Government approved ID
    bvn = CharField(_("Bank Verification Number"), blank=True, max_length=12)

    # address
    address = CharField(_("Kin Address"), max_length=500, blank=True, null=True)
    town = CharField(_("Kin Town/City"), max_length=120, blank=True, null=True)
    county = CharField(_("Kin County"), max_length=120, blank=True, null=True)
    state = CharField(_("Kin State"), max_length=120, blank=True, null=True)
    post_code = CharField(_("Kin Post Code"), max_length=120, blank=True, null=True)
    country = CharField(_("Kin Country"), max_length=120, blank=True, null=True)

    # Google Map
    longitude = FloatField(_("Kin Longitude"), default=0.00)
    latitude = FloatField(_("Kin Latitude"), default=0.00)

    gave_consent = BooleanField(
        _("Next of Kin has given consent to vouch for you"), default=False
    )
    kin_verified = BooleanField(default=False)

    @property
    def is_nest_of_kin_complete(self):
        try:
            profile = NextOfKin.objects.get(user=self.user)
            if (
                profile.image
                and profile.phone
                and profile.date_of_birth
                and profile.address
                and profile.town
                and profile.county
                and profile.state
                and profile.post_code
                and profile.country
                and profile.phone_verifed
            ):
                return True
        except NextOfKin.DoesNotExist:
            pass
        return False

    @property
    def kin_address(self):
        return f"{self.address}, {self.town}, {self.county}, {self.post_code}, {self.country}"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
            return age if age and age > 0 else 0
        return "NA"

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER NEXT OF KIN]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER NEXT OF KIN]"
        )

    class Meta:
        managed = True
        verbose_name = "User Next Of Kin"
        verbose_name_plural = "User Next Of Kin"
        ordering = ["-created"]


class RegisteredVehicles(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="vehicle", db_index=True)

    vehicle_manufacturer = CharField(_("Vehicle Make"), blank=True, max_length=500)
    vehicle_plate_no = CharField(_("Vehicle Plate Number"), blank=True, max_length=500)
    vehicle_color = CharField(_("Vehicle Plate Number"), blank=True, max_length=500)
    vehicle_type = OneToOneField(
        CarType,
        on_delete=CASCADE,
        related_name="vehicle_type",
        blank=True,
        null=True,
        db_index=True,
    )
    active = BooleanField(default=False)

    vehicle_verified = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username.upper()} {self.vehicle_plate_no}"

    class Meta:
        managed = True
        verbose_name = "Users Vehicle"
        verbose_name_plural = "Users Vehicles"
        ordering = ["-modified"]


class VerifiedDocuments(TimeStampedModel):
    user = OneToOneField(
        User, on_delete=CASCADE, related_name="documents", db_index=True
    )

    # Government approved ID
    license = CharField(_("Drivers License"), blank=True, max_length=50, db_index=True)
    license_exp = DateField(blank=True, null=True)

    # Vehicle Papers
    proof_of_ownership = FileField(
        upload_to="document/proof_of_ownership",
        validators=[validate_uploaded_pdf_extension],
        blank=True,
        null=True,
    )
    vehicle_license = FileField(
        upload_to="document/vehicle_license",
        validators=[validate_uploaded_pdf_extension],
        blank=True,
        null=True,
    )
    autocheck_certificate = FileField(
        upload_to="document/autocheck_certificate",
        validators=[validate_uploaded_pdf_extension],
        blank=True,
        null=True,
    )
    insurance = FileField(
        upload_to="document/insurance",
        validators=[validate_uploaded_pdf_extension],
        blank=True,
        null=True,
    )

    document_verified = BooleanField(_("Documents has been verified"), default=False)

    @property
    def percentage(self):
        total = 6
        id = 1 if self.nin or self.bvn else 0
        li = 1 if self.license else 0
        po = 1 if self.proof_of_ownership else 0
        vl = 1 if self.vehicle_license else 0
        ac = 1 if self.autocheck_certificate else 0
        ins = 1 if self.insurance else 0
        score = id + li + po + vl + ac + ins
        if score == 0:
            return 0
        return 100 * (total / score)

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER VERIFIED DOCUMENTS]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER VERIFIED DOCUMENTS]"
        )

    class Meta:
        managed = True
        verbose_name = "User Verified Documents"
        verbose_name_plural = "User Verified Documents"
        ordering = ["-created"]


class Wallet(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name="wallet", db_index=True)
    currency = ForeignKey(
        Currency,
        on_delete=CASCADE,
        related_name="wallet",
        verbose_name="Wallet Currency",
        null=True,
        blank=True,
        default=1,
        db_index=True,
    )

    balance = DecimalField(max_digits=20, decimal_places=2, default=0.00)
    old_balance = DecimalField(max_digits=20, decimal_places=2, default=0.00)
    margin = DecimalField(max_digits=20, decimal_places=2, default=0.00)
    profit = BooleanField(default=True)

    @property
    def pay_amount(self):
        return int(round(self.balance)) * 100

    @property
    def formated_wallet_balance(self):
        if self.currency.code != "USD":
            amount = self.currency.price * self.balance
            return f"{self.currency.symbol} {round(amount, 2)}"
        return f"{self.currency.symbol} {round(self.balance, 2)}"

    def __str__(self):
        return (
            f"{self.user.username.title()} [USER WALLET]"
            if not self.user.short_name
            else f"{self.user.short_name.title()} [USER WALLET]"
        )

    class Meta:
        managed = True
        verbose_name = "User Wallet"
        verbose_name_plural = "User Wallets"
        ordering = ["-modified"]


# _______________________________________________________________________________#
#                              Foreignkeys Relationship                         #
# _______________________________________________________________________________#
class BankAccount(TimeStampedModel):
    user = ForeignKey(
        User, on_delete=CASCADE, related_name="bank_account", db_index=True
    )
    bank = ForeignKey(
        Banks, on_delete=CASCADE, related_name="bank_account", db_index=True
    )
    acc_no = CharField(max_length=17, db_index=True)
    acc_name = CharField(max_length=255)

    bank_verified = BooleanField(default=False)
    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username.upper()} Saved Bank Account: {self.acc_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Bank"
        verbose_name_plural = "User Saved Banks"
        ordering = ["-modified"]


class SavedCards(TimeStampedModel):
    """Save transactional ATM Cards for use when ever making purchases

    Args:
        TimeStampedModel (_type_): _description_
    """

    user = ForeignKey(User, on_delete=CASCADE, related_name="saved_card", db_index=True)
    name_on_card = CharField(max_length=255)
    card_no = CharField(max_length=26, db_index=True)
    cvv = CharField(max_length=5, blank=True, null=True)
    card_exp_month = CharField(max_length=2, blank=True)
    card_exp_year = CharField(max_length=4, blank=True)
    card_provider = CharField(max_length=40, default="master")
    authorization_code = CharField(max_length=500, blank=True, null=True)

    active = BooleanField(default=False)
    card_verified = BooleanField(default=False)

    @property
    def exp_date(self):
        return f"{self.card_exp_month}-{self.card_exp_year}"

    @property
    def formatted_no(self):
        formatted = f"{self.card_no[:4]}-{self.card_no[4:8]}-{self.card_no[8:12]}-{self.card_no[12:]}"
        return formatted

    # TODO: Create a schedule task to delete this card if it has expired
    @property
    def expired(self):
        if (date.today().month, date.today().year) > (
            int(self.card_exp_month),
            int(self.card_exp_year),
        ):
            self.active = False
            self.save(update_fields=["active"])
            return True
        return False

    def __str__(self):
        return f"{self.user.username.upper()} Saved Card: {self.card_no}"

    class Meta:
        managed = True
        verbose_name = "User Saved Card"
        verbose_name_plural = "User Saved Cards"
        ordering = ["-created"]
