from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.test import TestCase
from rest_framework import serializers

from dropsride.users.api.serializers import (
    CustomPasswordResetSerializer,
    ReferralSerializer,
    UserLoginSerializer,
    UserRegistrationSerializer,
)
from dropsride.users.models import ReferralBonus

User = get_user_model()


class ReferralSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.referral = ReferralBonus.objects.create(user=self.user, amount=50)
        self.serializer = ReferralSerializer(instance=self.referral)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["amount", "user"])

    def test_amount_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["amount"], 50)

    def test_user_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["user"], "testuser")


class UserLoginSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
        )
        self.serializer = UserLoginSerializer()

    def test_valid_data(self):
        data = {
            "login": "testuser@example.com",
            "password": "testpass",
        }
        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["user"], self.user)

    def test_missing_email(self):
        data = {
            "password": "testpass",
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("login", serializer.errors)

    def test_missing_password(self):
        data = {
            "login": "testuser@example.com",
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_email(self):
        data = {
            "login": "nonexistent@example.com",
            "password": "testpass",
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("login", serializer.errors)

    def test_invalid_password(self):
        data = {
            "login": "testuser@example.com",
            "password": "wrongpass",
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)


class CustomPasswordResetSerializerTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )

    def test_valid_email(self):
        serializer = CustomPasswordResetSerializer(data={"email": self.user.email})
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["email"], self.user.email)

    def test_invalid_email(self):
        serializer = CustomPasswordResetSerializer(
            data={"email": "invalid@example.com"}
        )
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_password_reset_form(self):
        serializer = CustomPasswordResetSerializer(data={"email": self.user.email})
        serializer.is_valid(raise_exception=True)
        email = serializer.get_email_options()["email_template_name"]
        form = PasswordResetForm({"email": self.user.email})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.save(email_template_name=email), None)


class TestUserRegistrationSerializer:
    def test_serializer_valid(self):
        # Create mock data
        data = {
            "username": "john_doe",
            "email": "johndoe@example.com",
            "first_name": "John",
            "middle_name": "William",
            "last_name": "Doe",
            "gender": "M",
            "is_driver": True,
            "gave_consent": True,
            "password1": "password",
            "password2": "password",
        }

        # Instantiate the serializer with the mock data
        serializer = UserRegistrationSerializer(data=data)

        # Ensure that the serializer is valid
        assert serializer.is_valid() == True

        # Save the user
        user = serializer.save()

        # Ensure that the user is an instance of the User model
        assert isinstance(user, User) == True

        # Ensure that the user's fields match the mock data
        assert user.username == "john_doe"
        assert user.email == "johndoe@example.com"
        assert user.first_name == "John"
        assert user.middle_name == "William"
        assert user.last_name == "Doe"
        assert user.gender == "M"
        assert user.is_driver == True
        assert user.gave_consent == True

        # Ensure that the user's password is hashed
        assert user.password.startswith("pbkdf2_sha256")

    def test_serializer_invalid(self):
        # Create an existing user to cause validation errors
        User.objects.create_user(
            username="jane_doe", email="janedoe@example.com", password="password"
        )

        # Create mock data with an existing username and email
        data = {
            "username": "jane_doe",
            "email": "janedoe@example.com",
            "first_name": "Jane",
            "middle_name": "Marie",
            "last_name": "Doe",
            "gender": "F",
            "is_driver": False,
            "gave_consent": True,
            "password1": "password",
            "password2": "password",
        }

        # Instantiate the serializer with the mock data
        serializer = UserRegistrationSerializer(data=data)

        # Ensure that the serializer is invalid
        assert serializer.is_valid() == False

        # Ensure that the expected validation errors are present
        expected_errors = {
            "username": ["This username is already taken."],
            "email": ["This email is already taken."],
        }
        assert serializer.errors == expected_errors
