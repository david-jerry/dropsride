import pprint
from datetime import date, timedelta

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework import status
# from braces.views import CsrfExemptMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination  # , HttpResponsePermanentRedirect
from dropsride.transactions.models import Transaction

from ..models import TicketPlans, TicketSubscription
from .serializers import DriverSubscriptionSerializer, SubscriptionPlansSerializer

today = date.today()


class PlansViewset(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    """Here you create plans with unique localization parameter and by a given state outlining the duration for the plan and when it will expire in days

    Args:
        ListModelMixin (GET): Returns a list of all plans available to the
        RetrieveModelMixin (GET): Returns a plan detail by it's ID
        CreateModelMixin (POST): Posts a JSON object for a specific plan and returns the object as a JSON
    """

    serializer_class = SubscriptionPlansSerializer
    queryset = TicketPlans.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class SubscriptionViewset(
    RetrieveModelMixin,
    CreateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """API endpoint for drivers to subscribe to a ticket for a given state enabling them to make payments of the exact amount set out for that state. U must get the state name eihter by geolocating with google geocode or any means necessary.

    Example authorization window open to complete payment in Axios:
        to use axios to open the payment window do the below

        axios.get(payment_url)
            .then(response => {
                // Redirect the user to the payment page
                window.location = response.data.data.authorization_url;
            })
            .catch(error => {
                console.log(error);
            });

    Args:
        RetrieveModelMixin (GET): Returns a respons for just one JSON ticket object
        CreateModelMixin (POST): Posts an instance of the ticket subscribed to the endpoint and returns the ticket object as JSON
        ListModelMixin (GET): Returns a list of all tickets subscribed depending on the user role as superuser or just the tickets subscribed to by a single user

    """

    serializer_class = DriverSubscriptionSerializer
    queryset = TicketSubscription.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        user = self.request.user
        if user.is_staff:
            cache_key = "all_tickets"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset
                cache.set(cache_key, queryset)
        else:
            cache_key = f"tickets_{user.id}"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset.filter(driver=self.request.user)
                cache.set(cache_key, queryset)
        return queryset

    # custom action to retrieve the currenctly signed in users tickets
    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="my-tickets",
    )
    def my_tickets(self, request):
        tickets = self.queryset.filter(driver=request.user)
        if tickets:
            serializer = self.get_serializer(tickets, many=True)
            return Response(serializer.data)
        return Response({"message": "No tickets found."}, status=404)

    def create(self, request, *args, **kwargs):
        """Create the ticket first before requesting the payment authorization_url from paystack.

        NOTE: It is very important to get the state of the user by their geo coordinate to successfully get the plan from the backend as well as also get the choice of payment method either card or wallet

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.data["state"] != "":
            user = request.user
            plan = TicketPlans.objects.get(
                localization__state__state=request.data["state"]
            )
            serializer = DriverSubscriptionSerializer(
                data=request.data, context={"request": request}
            )
            serializer.save(driver=user, plan=plan)
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "data": serializer.data,
                    "message": "Processing Ticket",
                    "created": True,
                },
            )
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data={
                "message": "You have failed to allow location so we can not determine your state to assign a ticket plan.",
                "created": False,
            },
        )

    @action(detail=True, methods=["POST"])
    def pay(self, request, pk=None):
        """Make payments with paystack adding a custom callback_url to work with when the site requests to verify the payment

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        ticket = self.get_object()
        ttype = request.data["ttype"]

        wallet_balance_in_kobo = int(round(ticket.driver.wallet.wallet_balance) * 100)
        reference = f"tref-{ticket.driver.username}-{ticket.id}"
        amount_in_kobo = ticket.ticket_amount  # Convert to kobo (Paystack currency)

        if ticket.ticket_amount > 0 and ttype == "card":
            # Create Paystack payment request if the request is made by card else switch the payment processing to wallet assuming the wallet has adequate amoun to handle the payment else it will switch back to card payment
            headers = {
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
                "Content-Type": "application/json",
            }

            if request.user.saved_card.filter(active=True).exists():
                card = request.saved_card.filter(active=True).first()
                paystack_data = {
                    "email": request.user.email,
                    "amount": amount_in_kobo,
                    "reference": reference,
                    "channels": ["card", "ussd", "qr"],
                    "callback_url": f"{request.build_absolute_uri('/api/tickets/{pk}/verify/')}",
                    "authorization": {
                        "authorization_code": card.authorization_code,
                        "card_type": card.card_type,
                        "last4": card.last4,
                        "exp_month": card.exp_month,
                        "exp_year": card.exp_year,
                    },
                }

            else:
                paystack_data = {
                    "email": request.user.email,
                    "amount": amount_in_kobo,
                    "reference": reference,
                    "channels": ["card", "ussd", "qr"],
                    "callback_url": f"{request.build_absolute_uri('/api/tickets/{pk}/verify/')}",
                }
            response = requests.post(
                "https://api.paystack.co/transaction/initialize",
                json=paystack_data,
                headers=headers,
            )

            # Create transaction history
            if response.status_code == status.HTTP_200_OK:
                # convert response to json data
                json_response = response.json()

                if json_response["message"] == "Authorization URL created":
                    # add a transaction history for the card payment but set it to
                    Transaction.objects.create(
                        owner=ticket.driver,
                        amount=ticket.plan.amount,
                        transaction_reason=Transaction.TICKET,
                        transaction_status=Transaction.PENDING,
                        ref_code=json_response["reference"],
                        content_object=ticket,
                    )

                    # add an expiry date for the ticket and set the ticket status to active
                    expiry_date = today + timedelta(days=ticket.plan.duration)
                    ticket.expiry_date = expiry_date
                    ticket.status = TicketSubscription.ACTIVE
                    ticket.save(update_fields=["expiry_date", "status"])
                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            "message": json_response["message"],
                            "data": json_response["data"],
                        },
                    )

                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        "message": json_response["message"],
                        "data": json_response["data"],
                    },
                )

            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": response.message},
            )

        elif (
            ttype != "card"
            and ticket.ticket_amount > 0
            and wallet_balance_in_kobo >= amount_in_kobo
        ):
            # deduct the amount for the wallet
            ticket.driver.wallet.wallet_balance -= ticket.plan.amount
            ticket.driver.wallet.save(update_fields=["wallet_balance"])

            # create a transaction history for this payment
            Transaction.objects.create(
                owner=ticket.driver,
                amount=ticket.plan.amount,
                transaction_reason=Transaction.TICKET,
                transaction_status=Transaction.PAID,
                ref_code=reference,
                content_object=ticket,
            )

            # add an expiry date for the ticket and set the ticket status to active
            expiry_date = today + timedelta(days=ticket.plan.duration)
            ticket.expiry_date = expiry_date
            ticket.status = TicketSubscription.ACTIVE
            ticket.save(update_fields=["expiry_date", "status"])

            serializer = DriverSubscriptionSerializer(
                ticket, context={"request": request}
            )
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "message": f"Successfully paid for {ticket.plan.state} ticketing. Enabling driving access now",
                },
            )
        elif (
            ttype != "card"
            and ticket.ticket_amount > 0
            and wallet_balance_in_kobo < amount_in_kobo
        ):
            return Response(
                status=status.HTTP_402_PAYMENT_REQUIRED,
                data={
                    "message": "There is insufficient funds on your wallet. Please top it up before proceeding"
                },
            )

    @action(detail=True, methods=["GET"])
    def verify(self, request, pk=None):
        """
        API endpoint to verify if an initialized payment was successful, if successful it approves the ticket and then marks the transaction as verified or paid
        """
        ticket = self.get_object()
        transaction = Transaction.objects.filter(
            content_object=ticket, owner=ticket.driver
        ).latest("created")
        reference = request.query_params.get("reference")
        if not reference:
            return Response(
                {"error": "Paystack reference not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

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
                transaction.transaction_status = Transaction.PAID
                transaction.save(update_fields=["transaction_status"])
                expiry_date = today + timedelta(days=ticket.plan.duration)
                ticket.expiry_date = expiry_date
                ticket.status = TicketSubscription.ACTIVE
                ticket.save(update_fields=["expiry_date", "status"])
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "data": json_response["data"],
                        "message": json_response["message"],
                        "driver_status": True,
                    },
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "data": json_response["data"],
                    "message": json_response["message"],
                    "driver_status": False,
                },
            )

        return Response(
            status=response.status_code,
            data={"message": response.json()["message"], "driver_status": False},
        )


#     @action(
#         detail=True,
#         methods=["get", "post"],
#         permission_classes=[IsAuthenticatedOrReadOnly],
#     )
#     def enable(self, request, *args, **kwargs):
#         """
#         enable subscription requires subscription code and email token to enable.
#         NOTE: only successfully works after the charge has been successful else returns an error to the user/driver
#         """
#         obj = self.get_object()
#         authorization_code = request.data["authorization_code"]
#         ttype = request.data['ttype']
#         amount = int(request.data["amount"])
#         email = obj.driver.email


#         if ttype == "card":
#             url = "https://api.paystack.co/charge"
#             headers = {
#                 "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
#             }
#             data = {
#                 "email": email,
#                 "authorization_code": authorization_code,
#                 "amount": amount,
#             }
#             res = requests.request("POST", url, headers=headers, data=data)
#             res = res.json()
#             pp = pprint.PrettyPrinter(indent=4)
#             LOGGER.info(pp.pprint(res))
#             if (
#                 res["message"] == "Charge attempted"
#                 and res["data"]["status"] == "success"
#             ):
#                 Transaction.objects.create(
#                     owner=obj.driver,
#                     object=obj.id,
#                     amount=obj.plan.amount,
#                     transaction_reason=Transaction.TICKET,
#                     transaction_status=Transaction.PAID,
#                     ref_code=res["data"]['reference'],
#                 )

#                 expiry_date = today + timedelta(days=obj.plan.duration)
#                 obj.expiry_date = expiry_date
#                 obj.status = TicketSubscription.ACTIVE
#                 obj.save(update_fields=['expiry_date', 'status'])
#                 # serializer = DriverSubscriptionSerializer(
#                 #     obj, context={"request": request}
#                 # )
#                 return Response(
#                     status=status.HTTP_200_OK,
#                     data={
#                         # "data": serializer.data,
#                         "message": f"Successfully paid for ticketing. Enabling driving access now",
#                         "sub_id": obj.id,
#                     },
#                 )
#             elif res["data"]["status"] == "send_pin":
#                 return Response(
#                     status=status.HTTP_200_OK,
#                     data={
#                         "data": serializer.data,
#                         "message": f"Submit your PIN",
#                         "sub_id": obj.id,
#                         "ref": res["data"]["reference"],
#                     },
#                 )
#             elif res["data"]["status"] == "send_otp":
#                 return Response(
#                     status=status.HTTP_200_OK,
#                     data={
#                         "data": serializer.data,
#                         "message": f"Submit an OTP now",
#                         "sub_id": obj.id,
#                         "ref": res["data"]["reference"],
#                     },
#                 )
#             else:
#                 return Response(
#                     status=status.HTTP_400_BAD_REQUEST, data={"message": res["message"]}
#                 )

#         elif ttype == "wallet":
#             obj.driver.wallet.wallet_balance -= obj.plan.amount
#             obj.driver.wallet.save(update_fields=["wallet_balance"])
#             Transaction.objects.create(
#                 owner=obj.driver,
#                 object=obj.id,
#                 amount=obj.plan.amount,
#                 transaction_reason=Transaction.TICKET,
#                 transaction_status=Transaction.PAID,
#                 ref_code=obj.reference_code,
#             )

#             expiry_date = today + timedelta(days=obj.plan.duration)
#             obj.expiry_date = expiry_date
#             obj.status = TicketSubscription.ACTIVE
#             obj.save(update_fields=['expiry_date', 'status'])

#             serializer = DriverSubscriptionSerializer(obj, context={"request": request})
#             return Response(
#                 status=status.HTTP_200_OK,
#                 data={
#                     "data": serializer.data,
#                     "message": f"Successfully paid for ticketing. Enabling driving access now",
#                     "sub_id": obj.id,
#                 },
#             )


#     @action(
#         detail=True,
#         methods=["get", "post"],
#         permission_classes=[IsAuthenticatedOrReadOnly],
#     )
#     def charge(self, request, *args, **kwargs):
#         """This carges the user's wallet or authorized card for payment. Upon successful response, it enables the subscription plan for the user else it expires their subscription

#         Args:
#             request (POST): return the following kwargs [ttype, authotization_code, amount]
#         """
#         obj = self.get_object()
#         ref = request.data["ref"] if request.data["ref"] else None
#         otp = request.data["otp"] if request.data["otp"] else None
#         pin = request.data["pin"] if request.data["pin"] else None
#         if otp is not None:
#             url = "https://api.paystack.co/charge/submit_otp"
#             headers = {
#                 "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
#             }
#             data = {
#                 "reference": ref,
#                 "otp": otp,
#             }
#             res = requests.request("POST", url, headers=headers, data=data)
#             res = res.json()
#             pp = pprint.PrettyPrinter(indent=4)
#             LOGGER.info(pp.pprint(res))
#             if (
#                 res["message"] == "Charge attempted"
#                 and res["data"]["status"] == "success"
#             ):
#                 Transaction.objects.create(
#                     owner=obj.driver,
#                     object=obj.id,
#                     amount=obj.plan.amount,
#                     transaction_reason=Transaction.TICKET,
#                     transaction_status=Transaction.PAID,
#                     ref_code=obj.reference_code,
#                 )
#                 expiry_date = today + timedelta(days=obj.plan.duration)
#                 obj.expiry_date = expiry_date
#                 obj.status = TicketSubscription.ACTIVE
#                 obj.save(update_fields=['expiry_date', 'status'])
#                 # serializer = DriverSubscriptionSerializer(
#                 #     obj, context={"request": request}
#                 # )
#                 return Response(
#                     status=status.HTTP_200_OK,
#                     data={
#                         # "data": serializer.data,
#                         "message": f"Successfully paid for ticketing. Enabling driving access now",
#                         "sub_id": obj.id,
#                     },
#                 )

#         if pin is not None:
#             url = "https://api.paystack.co/charge/submit_pin"
#             headers = {
#                 "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
#             }
#             data = {
#                 "reference": ref,
#                 "pin": pin,
#             }
#             res = requests.request("POST", url, headers=headers, data=data)
#             res = res.json()
#             pp = pprint.PrettyPrinter(indent=4)
#             LOGGER.info(pp.pprint(res))
#             if (
#                 res["message"] == "Charge attempted"
#                 and res["data"]["status"] == "success"
#             ):
#                 Transaction.objects.create(
#                     owner=obj.driver,
#                     object=obj.id,
#                     amount=obj.plan.amount,
#                     transaction_reason=Transaction.TICKET,
#                     transaction_status=Transaction.PAID,
#                     ref_code=obj.reference_code,
#                 )
#                 expiry_date = today + timedelta(days=obj.plan.duration)
#                 obj.expiry_date = expiry_date
#                 obj.status = TicketSubscription.ACTIVE
#                 obj.save(update_fields=['expiry_date', 'status'])
#                 # serializer = DriverSubscriptionSerializer(
#                 #     obj, context={"request": request}
#                 # )
#                 return Response(
#                     status=status.HTTP_200_OK,
#                     data={
#                         # "data": serializer.data,
#                         "message": f"Successfully paid for ticketing. Enabling driving access now",
#                         "sub_id": obj.id,
#                     },
#                 )


# def verifypayment(request, *args, **kwargs):
#     ref = kwargs.get("ref")

#     plan_id = kwargs.get("plan_id")
#     url = f"https://api.paystack.co/transaction/verify/{ref}"
#     headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}

#     res = requests.request("GET", url, headers=headers)
#     res = res.json()
#     pp = pprint.PrettyPrinter(indent=4)
#     # TO LOG TO THE CONSOLE THE RESPONSE DATA
#     LOGGER.info(pp.pprint(res))
#     if res["data"]["status"] == "success":
#         return JsonResponse(
#             status=201,
#             data={
#                 "message": f"Payment has been made is successful",
#                 "plan_id": plan_id,
#                 "user_id": request.user.id,
#             },
#         )
#     else:
#         return JsonResponse(
#             status=400, data={"message": f"Payment was unsuccessful"}
#         )
