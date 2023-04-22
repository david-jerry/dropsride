import pprint

import requests
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from countries_plus.models import Country
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
# from braces.views import CsrfExemptMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.mixins import bvnVerify, ninVerify, phoneVerify
from config.pagination import CustomPagination
from dropsride.careers.api.serializers import (
    ApplicantSerializer,
    CareerSerializer,
    TeamSerializer,
)
from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.settings.models import Localization

User = get_user_model()


class TeamViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


class ApplicantViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = ApplicantSerializer
    queryset = Applicants.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


class CareerViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = CareerSerializer
    queryset = Careers.published.all_published_careers()
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    @action(detail=True, methods=["get", "post"], permission_classes=[AllowAny])
    def apply(self, request, *args, **kwargs):
        obj = self.get_object()
        first_name = request.data["first_name"]
        middle_name = request.data["middle_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        phone_number = request.data["phone_number"]
        gender = request.data["gender"]
        age = request.data["age"]
        location = Localization.objects.get(uuid=request.data["location"])
        file = request.data["file"]
        cover_letter = request.data["cover_letter"]
        disability = True if request.data["disability"] == "on" else False
        consent = True if request.data["consent"] == "on" else False
        country = Country.objects.get(iso=request.data["country"])
        Applicants.objects.create(
            position=obj,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            age=age,
            location=location,
            file=file,
            cover_letter=cover_letter,
            disability=disability,
            consent=consent,
            country=country,
        )
        serializer = CareerSerializer(obj, context={"request": request})
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "data": serializer.data,
                "message": f"You have applied for {obj.title.title()}",
            },
        )
