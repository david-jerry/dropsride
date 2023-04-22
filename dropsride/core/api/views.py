from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from dropsride.core.tasks import send_html_email

from .serializers import ContactSerializer


class ContactView(APIView):
    """
    Send support emails
    """

    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            send_html_email.delay(
                subject="SUPPORT MAIL",
                template="mails/support.html",
                from_email=f"{valid_data['company'].upper() or valid_data['name'].title()} <noreply@dropsride.com>",
                context={
                    "name": valid_data["name"].title(),
                    "phone": valid_data["phone"],
                    "email": valid_data["email"],
                    "message": valid_data["message"],
                },
                to_email=["support@dropsride.com"],
                reply_to=["support@dropsride.com"],
                attachment=None,
            )
            return Response(
                {"message": "Support Mail Successfully Sent", "title": "Support Mail"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Support Mail Failed to validate",
                "title": "SUPPORT EMAIL FAILED",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
