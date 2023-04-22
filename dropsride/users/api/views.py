from decimal import Decimal

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from dropsride.currency.models import Currency
from dropsride.transactions.models import Transaction
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
from dropsride.utils.logger import LOGGER
from dropsride.utils.utilities import convert_to_dollar

from .serializers import (
    BankAccountSerializer,
    NextOfKinSerializer,
    ProfileSerializer,
    ReferralSerializer,
    RegisteredVehiclesSerializer,
    SavedCardsSerializer,
    SettingsSerializer,
    UserSerializer,
    VerifiedDocumentsSerializer,
    WalletSerializer,
)

User = get_user_model()


class SettingsViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """A users settings endpoint to accept certain options like notification via email and the likes

    Args:
        RetrieveModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    lookup_field = "pk"  # or any other field you want to use for lookup
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user)


class NextOfKinViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """Endpoint to add a next of kin.

    Args:
        RetrieveModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    serializer_class = NextOfKinSerializer
    queryset = NextOfKin.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user)

    @action(detail=True, methods=["POST"])
    def confirm_consent(self, request, *args, **kwargs):
        """Endponit for the next of kin to accept the addition of their name into the system as a next of kin for the requesting driver"""
        next_of_kin = self.get_object()
        next_of_kin.gave_consent = True
        next_of_kin.save(update_fields=["gave_consent"])
        serializer = self.get_serializer(next_of_kin)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisteredVehiclesViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    """Endpoint to add a vehicle for verification. Verification can be done automatically but the team want to handle it manually. so they vet the cars themselves

    Args:
        ListModelMixin (_type_): _description_
        RetrieveModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    serializer_class = RegisteredVehiclesSerializer
    queryset = RegisteredVehicles.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        user = self.request.user
        if user.is_staff:
            cache_key = "all_vehicles"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset
                cache.set(cache_key, queryset)
        else:
            cache_key = f"vehicles_{user.id}"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset.filter(id=self.request.user.id)
                cache.set(cache_key, queryset)
        return queryset

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="my-vehicle",
    )
    def my_vehicle(self, request, *args, **kwargs):
        """enpoint to get just the authenticated user's vehicle detail

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        serializer = RegisteredVehiclesSerializer(
            request.user.vehicle, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class VerifiedDocumentsViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    """Endpoint to upload verifiable documents for the user. Like drivers license and the rest particulars for driving

    Args:
        ListModelMixin (_type_): _description_
        RetrieveModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    serializer_class = VerifiedDocumentsSerializer
    queryset = VerifiedDocuments.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        user = self.request.user
        if user.is_staff:
            cache_key = "all_documents"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset
                cache.set(cache_key, queryset)
        else:
            cache_key = f"documents_{user.id}"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset.filter(id=self.request.user.id)
                cache.set(cache_key, queryset)
        return queryset

    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="my-documents",
    )
    def my_documents(self, request, *args, **kwargs):
        """endpoint to get just the authenticated user's document and not all documents registered in the paltform

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        serializer = VerifiedDocumentsSerializer(
            request.user.documents, context={"request": request}
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class BankAccountViewSet(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """Endpoint to add a banck account that money will be apid into upon withdrawal request from the amount saved in teh wallet

    Args:
        ListModelMixin (_type_): _description_
        CreateModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        RetrieveModelMixin (_type_): _description_
        DestroyModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user)

    # custom action to retrieve the active bank account
    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="my-bank-account",
    )
    def active_account(self, request, *args, **kwargs):
        """Endpoint to get just the active account alone

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        active_account = self.queryset.filter(
            Q(user=request.user) & Q(active=True)
        ).first()
        if active_account:
            serializer = self.get_serializer(
                active_account, context={"request": request}
            )
            return Response(serializer.data)
        return Response({"message": "No active bank account found."}, status=404)

    # custom action to make all other bank accounts inactive when one bank account is made active
    @action(
        detail=True,
        methods=["PUT"],
        permission_classes=[IsAuthenticated],
        url_path="activate-bank-account",
    )
    def make_active(self, request, *args, **kwargs):
        """Endpoint to make a bank account active and the rest inavtive

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        pk = kwargs.get("pk")
        account = self.get_object()
        if account.user != request.user:
            return Response(
                {"message": "You do not have permission to perform this action."},
                status=403,
            )

        # make all other accounts inactive
        self.queryset.filter(Q(user=request.user) & ~Q(id=pk)).update(active=False)

        # make the selected account active
        account.active = True
        account.save(update_fields=["active"])

        serializer = self.get_serializer(account, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "You have activated this bank account.",
                "data": serializer.data,
            },
        )


class SavedCardsViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = SavedCards.objects.all()
    serializer_class = SavedCardsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination  # replace with your pagination class
    authentication_classes = [TokenAuthentication]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user)

    @action(
        detail=True,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="activate-card",
    )
    def make_active(self, request, *args, **kwargs):
        """Endpoint to make a debit card active and the rest active

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        card = self.get_object()
        pk = card.pk
        if card.user != request.user:
            return Response(
                data={"message": "You do not have permission to perform this action."},
                status=403,
            )

        # make all other accounts inactive
        self.queryset.filter(Q(user=request.user) & ~Q(id=pk)).update(active=False)

        # make the selected account active
        card.active = True
        card.save(update_fields=["active"])

        serializer = self.get_serializer(card, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "You have activated this debit card.",
                "data": serializer.data,
            },
        )

    @action(detail=True, methods=["GET"])
    def pay(self, request, *args, **kwargs):
        """
        API endpoint to make payment using Paystack API and retrieve authorization code for a card
        """
        card = self.get_object()
        reference = f"Cref-{card.user.username}-{card.id}"
        amount = 50 * 100  # TO CONVERT TO KOBO FOR PAYSTACK
        if not amount:
            return Response(
                {"error": "Amount not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Initialize Paystack payment
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "email": request.user.email,
            "amount": amount,
            "reference": reference,
            "callback_url": f"{request.build_absolute_uri(f'/cards/verify/?t={card.user.token}&p={card.pk}')}",
            "metadata": {
                "user_id": request.user.id,
                "card_id": card.id,
            },
        }
        response = requests.post(
            "https://api.paystack.co/transaction/initialize", headers=headers, json=data
        )

        # Serve authorization URL in a window popup
        if response.status_code == status.HTTP_200_OK:
            # convert the response to json
            json_response = response.json()

            # get the authorization url for window pop up and payment completion
            authorization_url = json_response["data"]["authorization_url"]
            res_reference = json_response["data"]["reference"]

            # create a pending transaction history
            amount = convert_to_dollar(50.00)
            Transaction.objects.create(
                owner=card.user,
                amount=amount,
                transaction_reason=Transaction.CARD,
                transaction_status=Transaction.PENDING,
                ref_code=json_response["data"]["reference"],
                content_object=card,
            )
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "authorization_url": authorization_url,
                    "reference": res_reference,
                },
            )

        return Response(status=response.status_code, data=response.json())

    @action(detail=True, methods=["GET"], permission_classes=[AllowAny])
    def verify(self, request, *args, **kwargs):
        """
        API endpoint to verify if an initialized payment was successful, if successful it makes the card verified
        """
        card = self.get_object()
        reference = request.query_params.get("reference")

        if not reference:
            return Response(
                {"message": "Paystack reference not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        transaction = Transaction.objects.filter(
            owner=card.user, ref_code=reference
        ).latest("created")

        # Verify Paystack payment
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.get(
            f"https://api.paystack.co/transaction/verify/{reference}", headers=headers
        )

        # Update transaction history
        if response.status_code == status.HTTP_200_OK:
            json_response = response.json()
            if json_response["data"]["status"] == "success":
                # update the transaction status if successfully paid
                transaction.transaction_status = Transaction.PAID
                transaction.save(update_fields=["transaction_status"])

                # add the card amount to the user's wallet
                card.user.wallet.balance += convert_to_dollar(50.00)
                card.authorization_code = json_response["data"]["authorization"][
                    "authorization_code"
                ]
                card.user.wallet.save(update_fields=["balance"])

                # update teh card status to verified since it was a successful payment made by the card
                card.card_verified = True
                card.active = True
                card.save(update_fields=["active", "card_verified"])
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "data": json_response["data"],
                        "message": json_response["message"],
                    },
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "data": json_response["data"],
                    "message": json_response["message"],
                },
            )

        return Response(
            status=response.status_code, data={"message": response.json()["message"]}
        )


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    """Enpoint to get user details either as a staff or a specific user

    Args:
        RetrieveModelMixin (_type_): _description_
        ListModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        user = self.request.user
        if user.is_staff:
            cache_key = "all_users"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset
                cache.set(cache_key, queryset)
        else:
            cache_key = f"users_{user.id}"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset.filter(id=self.request.user.id)
                cache.set(cache_key, queryset)
        return queryset

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        """endpoint to get just the authenticated users detail"""
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["POST"], permission_classes=[IsAuthenticated])
    def driver(self, request, *args, **kwargs):
        """endpoint to get toggle drivers mode"""
        user = request.user
        user.is_driver = True if request.data.get("toggle") == "true" else False
        user.save(update_fields=["is_driver"])
        message = "Toggled Driver Mode" if user.is_driver else "Toggled Rider Mode"
        serializer = UserSerializer(user, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data, "message": message},
        )

    @action(detail=False, methods=["POST"], permission_classes=[IsAuthenticated])
    def currency(self, request, *args, **kwargs):
        """endpoint to switch the currency"""
        user = request.user
        cur = get_object_or_404(Currency, id=request.data["currency"])
        user.wallet.currency = cur
        user.wallet.save(update_fields=["currency"])
        message = "Currency changed successfully"
        serializer = UserSerializer(user, context={"request": request})
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data, "message": message},
        )

    @action(
        detail=True,
        methods=["PUT", "POST", "PATCH"],
        permission_classes=[IsAuthenticated],
        url_path="update-image",
    )
    def update_image(self, request, *args, **kwargs):
        """
        Endpoint to update the users profile image
        """
        user = request.user
        profile = user.profile
        image = request.data.get("image")
        if image:
            profile.image = image
            profile.save(update_fields=["image"])
            serializer = UserSerializer(user, context={"request": request})
            url = user.get_absolute_url()
            return Response(
                {
                    "data": serializer.data,
                    "message": "Updated your profile image",
                    "url": url,
                }
            )
        serializer = UserSerializer(user, context={"request": request})
        return Response(
            {"data": serializer.data, "message": "Image updating failed", "url": url}
        )

    @action(detail=True, methods=["GET"], permission_classes=[IsAuthenticated])
    def deactivate(self, request, *args, **kwargs):
        """
        Enpoint to deactivate a user account
        """
        user = self.get_object()
        user.is_active = False
        user.save(update_fields=["is_active"])
        serializer = UserSerializer(user, context={"request", request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                "data": serializer.data,
                "message": 'Your account has been deactivated. You won\'t be able to login or signup with the same email. <a href="/support/">Contact support for assistance.</a>',
            },
        )

    @action(
        detail=True,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="delete-account",
    )
    def delete_account(self, request, *args, **kwargs):
        """
        Endpoint to delete all user details from the system
        """
        user = self.get_object()
        user.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": 'Your account has been deleted. You won\'t be able to login the same email. <a href="/support/">Contact support for assistance.</a>'
            },
        )
