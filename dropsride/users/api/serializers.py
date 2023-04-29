from datetime import date
from difflib import SequenceMatcher

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer
from django.contrib.auth import authenticate, get_user_model
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers

from config.mixins import (
    accVerify,
    bvnVerify,
    driverLicenseVerify,
    ninVerify,
    phoneVerify,
)
from dropsride.core.tasks import send_html_email
from dropsride.users.models import (
    BankAccount,
    NextOfKin,
    Profile,
    ReferralBonus,
    RegisteredVehicles,
    SavedCards,
    Settings,
    VerifiedDocuments,
    Wallet,
)
from dropsride.users.tasks import verify_user_phone
from dropsride.utils.logger import LOGGER

User = get_user_model()
today = date.today()


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralBonus
        fields = ["amount"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = [
            "sms_notification",
            "email_notification",
            "push_notification",
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret


class ProfileSerializer(serializers.ModelSerializer):
    is_profile_complete = serializers.ReadOnlyField()
    home_address = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = (
            "image",
            "phone",
            "date_of_birth",
            "address",
            "town",
            "bvn",
            "county",
            "state",
            "post_code",
            "country",
            "profile_verified",
            "is_profile_complete",
            "home_address",
            "age",
        )
        read_only_fields = ("is_profile_complete", "home_address", "age")

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret

    # def validate(self, data):
    #     """
    #     Check that the users shortname is similar to the verified shortname returned from you verify as well as the Date of birth.
    #     to be passed to a celery worker to check the user detail and allow or delete the phone number details depending on what was returned
    #     """
    #     verify_user_phone.delay(
    #         dob=data["date_of_birth"],
    #         phone=data["phone"],
    #         short_name=self.context["request"].user.short_name,
    #         email=self.context["request"].user.email,
    #     )
    #     return data


class NextOfKinSerializer(serializers.ModelSerializer):
    kin_address = serializers.ReadOnlyField()
    is_nest_of_kin_complete = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()

    class Meta:
        model = NextOfKin
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "age",
            "email",
            "phone",
            "bvn",
            "address",
            "town",
            "county",
            "state",
            "post_code",
            "country",
            "longitude",
            "latitude",
            "gave_consent",
            "kin_verified",
            "kin_address",
            "is_nest_of_kin_complete",
        ]
        read_only_fields = [
            "kin_address",
            "is_nest_of_kin_complete",
            "age",
            "kin_verified",
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret

    # def validate(self, data):
    #     """
    #     Check that the kin shortname is similar to the verified shortname returned from you verify as well as the Date of birth.
    #     to be passed to a celery worker to check the detail and allow or delete the phone number details depending on what was returned
    #     """
    #     sn = data["first_name"] + " " + data["last_name"]
    #     verify_user_phone.delay(
    #         dob=data["date_of_birth"],
    #         phone=data["phone"],
    #         short_name=str(sn),
    #         email=data["email"],
    #     )
    #     return data


class RegisteredVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredVehicles
        fields = [
            "vehicle_manufacturer",
            "vehicle_plate_no",
            "vehicle_color",
            "vehicle_type",
            "vehicle_verified",
            "active",
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret


class VerifiedDocumentsSerializer(serializers.ModelSerializer):
    percentage = serializers.ReadOnlyField()

    class Meta:
        model = VerifiedDocuments
        fields = [
            "user",
            "license",
            "license_exp",
            "proof_of_ownership",
            "vehicle_license",
            "autocheck_certificate",
            "insurance",
            "document_verified",
            "percentage",
        ]

    # TODO: Create validation to validate the license of the user and ensure the validated data bears a strong similarity to the user

    def validate_license_exp(self, value):
        LOGGER.info(value)
        LOGGER.info(date.today())
        if value < date.today():
            raise serializers.ValidationError("License has already expired")
        return value

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret

    def update(self, instance, validated_data):
        # Ensure the user cannot update the `user`
        validated_data.pop("user", None)
        return super().update(instance, validated_data)


class WalletSerializer(serializers.ModelSerializer):
    pay_amount = serializers.SerializerMethodField()
    formated_wallet_balance = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = [
            "user",
            "currency",
            "balance",
            "old_balance",
            "pay_amount",
            "formated_wallet_balance",
            "margin",
            "profit",
        ]

    def get_pay_amount(self, obj):
        return int(round(obj.balance)) * 100

    def get_formated_wallet_balance(self, obj):
        if obj.currency.code != "USD":
            amount = obj.currency.price * obj.balance
            return f"{obj.currency.symbol} {round(amount, 2)}"
        return f"{obj.currency.symbol} {round(obj.balance, 2)}"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ("id", "acc_no", "acc_name", "bank_verified", "active")

    def validate_acc_no(self, value):
        """
        Validate the account number.
        """
        # Ensure the account number only contains digits
        if not value.isdigit():
            raise serializers.ValidationError("Account number can only contain digits")

        # Ensure the account number is the correct length for the specified bank
        bank = self.initial_data.get("bank")
        if bank and len(value) != bank.account_length:
            raise serializers.ValidationError(
                "Account number length is incorrect for the specified bank"
            )

        return value

    def validate_acc_name(self, value):
        """
        Validate the account name.
        """
        # Ensure the account name only contains letters, spaces, and hyphens
        if not all(c.isalpha() or c.isspace() or c == "-" for c in value):
            raise serializers.ValidationError(
                "Account name can only contain letters, spaces, and hyphens"
            )

        # ensure the bank name is similar to the user's account name
        acc_name = value
        user_name = self.context["request"].user.long_name
        similarity_ratio = SequenceMatcher(
            None, acc_name.lower(), user_name.lower()
        ).ratio()
        if similarity_ratio < 0.7:
            raise serializers.ValidationError(
                "The name on the bank account and the name of the user are not similar enough."
            )
        return value

    # TODO: Create validator to validate the bank account number and check the nameon the bank account with the user's name if valid updates the user's bank_verified status to True else it stays false

    def create(self, validated_data):
        # Associate the bank account with the current user
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Ensure the user cannot update the `user` or `bank` fields
        validated_data.pop("user", None)
        validated_data.pop("bank", None)
        return super().update(instance, validated_data)


class SavedCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCards
        fields = [
            "id",
            "name_on_card",
            "card_no",
            "card_exp_month",
            "card_exp_year",
            "cvv",
            "card_provider",
            "card_verified",
            "authorization_code",
            "exp_date",
            "formatted_no",
            "expired",
        ]
        read_only_fields = [
            "id",
            "authorization_code",
            "exp_date",
            "formatted_no",
            "expired",
        ]
        extra_kwargs = {
            "name_on_card": {"required": True},
            "card_no": {"required": True},
            "card_exp_month": {"required": True},
            "card_exp_year": {"required": True},
            "card_provider": {"required": True},
        }

    def validate_card_no(self, value):
        if SavedCards.objects.filter(card_no=value).exists():
            raise serializers.ValidationError("Card number already exists.")
        if not len(value) >= 16:
            raise serializers.ValidationError("Card number should be 16 digits long.")
        return value

    def validate(self, data):
        # TODO: validate the card from paystack and ensure the card bears a similarity to the registered user

        # Validate that the name on the card and the name of the user are very similar
        LOGGER.info(data)
        name_on_card = data.get("name_on_card", "")
        LOGGER.info(data.get("name_on_card", ""))
        user_name = self.context["request"].user.long_name
        similarity_ratio = SequenceMatcher(
            None, name_on_card.lower(), user_name.lower()
        ).ratio()
        if similarity_ratio < 0.7:
            raise serializers.ValidationError(
                "The name on the card and the name of the user are not similar enough."
            )

        # Validate the month and the year to ensure the card has not expired already
        card_exp_month = data.get("card_exp_month", "")
        card_exp_year = data.get("card_exp_year", "")
        if card_exp_month and card_exp_year:
            if (date.today().month, date.today().year) > (
                int(card_exp_month),
                int(card_exp_year),
            ):
                raise serializers.ValidationError("The card has already expired.")

        # Ensure that the CVV is not exposed in the response
        # if "cvv" in self.initial_data:
        #     raise serializers.ValidationError(
        #         "CVV should not be included in the request."
        #     )
        return data

    def create(self, validated_data):
        return SavedCards.objects.create(
            user=self.context["request"].user, **validated_data
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret

    def update(self, instance, validated_data):
        # Ensure the user cannot update the `user`
        validated_data.pop("user", None)
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    recommended_by = serializers.StringRelatedField()

    ref_bonus = ReferralSerializer(many=False, read_only=True)
    settings = SettingsSerializer(many=False, read_only=True)
    profile = ProfileSerializer()
    nok = NextOfKinSerializer(many=False, read_only=True)
    vehicle = RegisteredVehiclesSerializer(many=False, read_only=True)
    documents = VerifiedDocumentsSerializer(many=False, read_only=True)
    wallet = WalletSerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=True, read_only=True)
    saved_card = SavedCardsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "unique_id",
            "ref_number",
            "gender",
            "recommended_by",
            "ref_link",
            "referrals",
            "customer_code",
            "longitude",
            "latitude",
            # bolean fields
            "is_driver",
            "is_verified",
            "gave_consent",
            "on_a_ride",
            "email_verified",
            # methods
            "name_initials",
            "short_name",
            "long_name",
            # onetoone relationships
            "ref_bonus",
            "settings",
            "profile",
            "nok",
            "vehicle",
            "documents",
            "wallet",
            "bank_account",
            "saved_card",
            "token",
            "url",
        )

        read_only_fields = [
            "name_initials",
            "short_name",
            "long_name",
            "username",
            "nok",
            "ref_bonus",
            "settings",
            "vehicle",
            "documents",
            "wallet",
            "bank_account",
            "saved_card",
            "email",
            "token",
            "recommended_by",
            "ref_link",
            "referrals",
            "customer_code",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
            "profile": {"required": False},
        }

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile', {})
    #     for attr, value in profile_data.items():
    #         setattr(instance.profile, attr, value)
    #     instance.profile.save()
    #     return super().update(instance, validated_data)

    def update(self, instance, validated_data):
        # Extract the profile data from the validated data
        profile_data = validated_data.pop("profile", None)

        # Call the parent's update method to update the User instance
        instance = super().update(instance, validated_data)

        # If profile data was provided, update the related Profile instance
        if profile_data is not None:
            profile_serializer = ProfileSerializer(
                instance.profile,
                data=profile_data,
                partial=True,  # Allow partial updates
            )
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()

        return instance


class UserRegistrationSerializer(RegisterSerializer):
    """Registration serializer with gender and boolean field to toggle between driver and rider"""

    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.ChoiceField(choices=User.GENDER)
    is_driver = serializers.BooleanField()
    gave_consent = serializers.BooleanField()

    def create(self, validated_data):
        validated_data.pop("password2", None)
        return super().create(validated_data)

    def validate(self, data):
        errors = {}

        # Check if the username already exists
        if User.objects.filter(username=data.get("username")).exists():
            errors["username"] = ["This username is already taken."]

        # Check if the email already exists
        if User.objects.filter(email=data.get("email")).exists():
            errors["email"] = ["This email is already taken."]

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data["first_name"]
        user.middle_name = self.validated_data["middle_name"]
        user.last_name = self.validated_data["last_name"]
        user.gender = self.validated_data["gender"]
        user.is_driver = self.validated_data["is_driver"]
        user.gave_consent = self.validated_data["gave_consent"]
        user.save()
        return user


class UserLoginSerializer(LoginSerializer):
    """To log a user in"""

    login = serializers.EmailField()

    def validate(self, attrs):
        LOGGER.info(attrs)
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                msg = "The email address is not assigned to any user. You can switch to signup for a new account."
                raise serializers.ValidationError(msg, code="authorization")

            if not user.check_password(password):
                msg = "Invalid credentials. The email or password is wrong. Try confirming you are correct or else request for a password reset."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = "Please provide both email and password."
            raise serializers.ValidationError(msg)

        attrs["user"] = user
        return attrs


class CustomPasswordResetSerializer(PasswordResetSerializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    def validate_email(self, value):
        value = super().validate_email(value)

        LOGGER.info(value)

        UserModel = get_user_model()
        try:
            UserModel.objects.get(email=value)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(_("Email address not found"))

        return value

    def get_email_options(self):
        return {
            "email_template_name": "registration/password_reset_email.html",
        }
